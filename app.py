import os
import json
import functools

from flask import Flask, render_template, request, jsonify, Response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin")
GCS_BUCKET = os.environ.get("GCS_BUCKET")
CONTENT_FILE = os.path.join(os.path.dirname(__file__), "content.json")
SEED_FILE = os.path.join(os.path.dirname(__file__), "content_seed.json")


def _gcs_blob():
    from google.cloud import storage
    client = storage.Client()
    return client.bucket(GCS_BUCKET).blob("content.json")


def _load_seed():
    with open(SEED_FILE) as f:
        return json.load(f)


def get_content():
    if GCS_BUCKET:
        blob = _gcs_blob()
        if blob.exists():
            return json.loads(blob.download_as_text())
        content = _load_seed()
        save_content(content)
        return content
    else:
        if os.path.exists(CONTENT_FILE):
            with open(CONTENT_FILE) as f:
                return json.load(f)
        content = _load_seed()
        save_content(content)
        return content


def save_content(content):
    if GCS_BUCKET:
        blob = _gcs_blob()
        blob.upload_from_string(
            json.dumps(content, indent=2, ensure_ascii=False),
            content_type="application/json",
        )
    else:
        with open(CONTENT_FILE, "w") as f:
            json.dump(content, f, indent=2, ensure_ascii=False)


def require_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.password != ADMIN_PASSWORD:
            return Response(
                "Authentication required.",
                401,
                {"WWW-Authenticate": 'Basic realm="Admin"'},
            )
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def index():
    content = get_content()
    return render_template("landing.html", content=content)


@app.route("/admin")
@require_auth
def admin():
    content = get_content()
    return render_template("admin.html", content=content)


@app.route("/admin/save", methods=["POST"])
@require_auth
def admin_save():
    content = request.get_json()
    if not content:
        return jsonify({"error": "No content provided"}), 400
    save_content(content)
    return jsonify({"success": True})


@app.route("/admin/reset", methods=["POST"])
@require_auth
def admin_reset():
    content = _load_seed()
    save_content(content)
    return jsonify({"success": True})


@app.route("/admin/pages/<slug>/delete", methods=["POST"])
@require_auth
def admin_delete_page(slug):
    content = get_content()
    content.setdefault("pages", [])
    content["pages"] = [p for p in content["pages"] if p.get("slug") != slug]
    save_content(content)
    return jsonify({"success": True})


@app.route("/<slug>")
def custom_page(slug):
    content = get_content()
    pages = content.get("pages", [])
    page = next((p for p in pages if p.get("slug") == slug), None)
    if page is None:
        return render_template("landing.html", content=content), 404
    return render_template("page.html", content=content, page=page)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG", "0") == "1")
