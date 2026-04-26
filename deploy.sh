#!/usr/bin/env bash
# One-command Cloud Run deployment for LearnUps
# Usage: ADMIN_PASSWORD=yourpass ./deploy.sh
set -euo pipefail

# Load .env if it exists
if [[ -f "$(dirname "$0")/.env" ]]; then
  set -a
  source "$(dirname "$0")/.env"
  set +a
fi

PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-$(gcloud config get-value project 2>/dev/null)}"
SERVICE_NAME="${SERVICE_NAME:-learnups}"
REGION="${REGION:-us-central1}"
IMAGE="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"
ADMIN_PW="${ADMIN_PASSWORD:-changeme}"

if [[ -z "$PROJECT_ID" ]]; then
  echo "ERROR: Set GOOGLE_CLOUD_PROJECT or configure gcloud default project."
  exit 1
fi

echo "=== LearnUps Cloud Run Deploy ==="
echo "Project : $PROJECT_ID"
echo "Service : $SERVICE_NAME"
echo "Region  : $REGION"
echo "Image   : $IMAGE"
echo ""

# Enable required APIs (safe to run multiple times)
echo "→ Enabling required APIs..."
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  firestore.googleapis.com \
  containerregistry.googleapis.com \
  --project "$PROJECT_ID" --quiet

# Create Firestore database if it doesn't exist yet
echo "→ Ensuring Firestore database exists..."
gcloud firestore databases create --location=nam5 --project "$PROJECT_ID" --quiet 2>/dev/null || true

# Build & push image using Cloud Build
echo "→ Building image..."
gcloud builds submit --tag "$IMAGE" --project "$PROJECT_ID"

# Deploy to Cloud Run
echo "→ Deploying to Cloud Run..."
gcloud run deploy "$SERVICE_NAME" \
  --image "$IMAGE" \
  --platform managed \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars "GOOGLE_CLOUD_PROJECT=${PROJECT_ID},ADMIN_PASSWORD=${ADMIN_PW},GCS_BUCKET=learnups-content-savvy" \
  --project "$PROJECT_ID"

URL=$(gcloud run services describe "$SERVICE_NAME" \
  --region "$REGION" \
  --project "$PROJECT_ID" \
  --format "value(status.url)")

echo ""
echo "=== Deployed successfully! ==="
echo "Landing page : $URL"
echo "Admin panel  : ${URL}/admin"
echo ""
echo "Login with password: $ADMIN_PW"
