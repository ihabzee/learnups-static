#!/usr/bin/env python3
"""
One-time script: converts learnups-landing_4.html → templates/landing.html
Run once: python make_template.py
"""

SRC = "learnups-landing_4.html"
DST = "templates/landing.html"

with open(SRC, encoding="utf-8") as f:
    html = f.read()

warns = []

def rep(old, new):
    global html
    if old not in html:
        warns.append(f"  NOT FOUND: {old[:60]!r}")
        return
    html = html.replace(old, new, 1)


# ── HEAD ─────────────────────────────────────────────────────────────────────

rep(
    "<title>LearnUps — Low-Cost Homework & Assessment System</title>",
    "<title>{{ content.meta.title }}</title>",
)

# ── NAV ──────────────────────────────────────────────────────────────────────

rep(
    '    <div class="nav-links">\n'
    '      <a href="#features">Features</a>\n'
    '      <a href="#educators">For Educators</a>\n'
    '      <a href="#students">For Students</a>\n'
    '      <a href="#pricing">Pricing</a>\n'
    '      <a href="#contact">Contact</a>\n'
    '    </div>',
    '    <div class="nav-links">\n'
    '      {% for link in content.nav.links %}\n'
    '      <a href="{{ link.href }}">{{ link.text }}</a>\n'
    '      {% endfor %}\n'
    '    </div>',
)

rep(
    '      <a href="#" class="btn-ghost">Log In</a>',
    '      <a href="{{ content.nav.btn_login_href }}" class="btn-ghost">{{ content.nav.btn_login }}</a>',
)

rep(
    '      <a href="#" class="btn-primary">Get Started →</a>',
    '      <a href="{{ content.nav.btn_signup_href }}" class="btn-primary">{{ content.nav.btn_signup }}</a>',
)

# ── HERO ─────────────────────────────────────────────────────────────────────

rep(
    "Trusted by educators across the US",
    "{{ content.hero.badge }}",
)

rep(
    "<h1>Smarter homework.<br>Simpler grading.<br><em>Tiny price.</em></h1>",
    "<h1>{{ content.hero.h1_line1 }}<br>{{ content.hero.h1_line2 }}<br><em>{{ content.hero.h1_line3_em }}</em></h1>",
)

rep(
    "LearnUps is a low-cost online homework and assessment platform built for educators who want meaningful student data — without the enterprise price tag.",
    "{{ content.hero.subtitle }}",
)

rep(
    '        <a href="#" class="btn-hero-primary">Start Free Trial →</a>',
    '        <a href="{{ content.hero.btn_primary_href }}" class="btn-hero-primary">{{ content.hero.btn_primary }}</a>',
)

rep(
    '        <a href="#features" class="btn-hero-outline">See How It Works</a>',
    '        <a href="{{ content.hero.btn_secondary_href }}" class="btn-hero-outline">{{ content.hero.btn_secondary }}</a>',
)

# Hero stats
rep(
    '<div class="hero-stats">\n'
    '        <div class="stat-item">\n'
    '          <div class="stat-num">10<span>K+</span></div>\n'
    '          <div class="stat-label">Active students</div>\n'
    '        </div>\n'
    '        <div class="stat-item">\n'
    '          <div class="stat-num">50<span>+</span></div>\n'
    '          <div class="stat-label">Question types</div>\n'
    '        </div>\n'
    '        <div class="stat-item">\n'
    '          <div class="stat-num">$<span>0</span></div>\n'
    '          <div class="stat-label">Student cost</div>\n'
    '        </div>\n'
    '      </div>',
    '<div class="hero-stats">\n'
    '        <div class="stat-item">\n'
    '          <div class="stat-num">{{ content.hero.stat1_num }}</div>\n'
    '          <div class="stat-label">{{ content.hero.stat1_label }}</div>\n'
    '        </div>\n'
    '        <div class="stat-item">\n'
    '          <div class="stat-num">{{ content.hero.stat2_num }}</div>\n'
    '          <div class="stat-label">{{ content.hero.stat2_label }}</div>\n'
    '        </div>\n'
    '        <div class="stat-item">\n'
    '          <div class="stat-num">{{ content.hero.stat3_num }}</div>\n'
    '          <div class="stat-label">{{ content.hero.stat3_label }}</div>\n'
    '        </div>\n'
    '      </div>',
)

# ── TRUST BAR ────────────────────────────────────────────────────────────────

rep(
    "<p>Integrates seamlessly with your existing LMS</p>",
    "<p>{{ content.trust_bar.label }}</p>",
)

rep(
    '  <div class="trust-logos">\n'
    '    <span class="trust-logo">Canvas LMS</span>\n'
    '    <span class="trust-logo">·</span>\n'
    '    <span class="trust-logo">Moodle</span>\n'
    '    <span class="trust-logo">·</span>\n'
    '    <span class="trust-logo">Blackboard</span>\n'
    '    <span class="trust-logo">·</span>\n'
    '    <span class="trust-logo">Brightspace</span>\n'
    '    <span class="trust-logo">·</span>\n'
    '    <span class="trust-logo">Open edX</span>\n'
    '  </div>',
    '  <div class="trust-logos">\n'
    '    {% for logo in content.trust_bar.logos %}\n'
    '    <span class="trust-logo">{{ logo }}</span>\n'
    '    {% if not loop.last %}<span class="trust-logo">·</span>{% endif %}\n'
    '    {% endfor %}\n'
    '  </div>',
)

# ── FEATURES ─────────────────────────────────────────────────────────────────

rep(
    '      <div class="section-tag">Why LearnUps</div>',
    '      <div class="section-tag">{{ content.features.tag }}</div>',
)

rep(
    '<h2 class="section-title">Everything you need.<br>Nothing you don\'t.</h2>',
    '<h2 class="section-title">{{ content.features.title | safe }}</h2>',
)

rep(
    "Purpose-built for instructors who want a powerful, flexible, and affordable assessment tool — not a bloated enterprise suite.",
    "{{ content.features.subtitle }}",
)

rep(
    '    <div class="feature-grid">\n'
    '      <div class="feature-card">\n'
    '        <div class="feature-icon">📋</div>\n'
    '        <h3>Diverse Question Types</h3>\n'
    '        <p>Multiple choice, short answer, fill-in-the-blank, matching, ordering, and more — all serving different learning outcomes to meet pedagogical goals.</p>\n'
    '      </div>\n'
    '      <div class="feature-card">\n'
    '        <div class="feature-icon">⚡</div>\n'
    '        <h3>Instant Auto-Grading</h3>\n'
    '        <p>Save hours every week. LearnUps automatically grades submissions and syncs scores back to your LMS grade book in real time.</p>\n'
    '      </div>\n'
    '      <div class="feature-card">\n'
    '        <div class="feature-icon">📊</div>\n'
    '        <h3>Deep Analytics</h3>\n'
    '        <p>See which questions students struggle with most. Track performance trends, identify learning gaps, and iterate on your content.</p>\n'
    '      </div>\n'
    '      <div class="feature-card">\n'
    '        <div class="feature-icon">🔗</div>\n'
    '        <h3>LTI Integration</h3>\n'
    '        <p>Connect LearnUps to Canvas, Moodle, or any LTI-compatible LMS with a few clicks. Grades sync automatically — no manual exports.</p>\n'
    '      </div>\n'
    '      <div class="feature-card">\n'
    '        <div class="feature-icon">📚</div>\n'
    '        <h3>Open Education Resources</h3>\n'
    '        <p>Adopt OER content and we\'ll help you build assessments around it — saving you weeks of question-writing time.</p>\n'
    '      </div>\n'
    '      <div class="feature-card">\n'
    '        <div class="feature-icon">🛡️</div>\n'
    '        <h3>Academic Integrity</h3>\n'
    '        <p>Randomized question pools, time limits, and per-student question shuffling make every attempt unique and harder to share answers.</p>\n'
    '      </div>\n'
    '    </div>',
    '    <div class="feature-grid">\n'
    '      {% for card in content.features.cards %}\n'
    '      <div class="feature-card">\n'
    '        <div class="feature-icon">{{ card.icon }}</div>\n'
    '        <h3>{{ card.title }}</h3>\n'
    '        <p>{{ card.desc }}</p>\n'
    '      </div>\n'
    '      {% endfor %}\n'
    '    </div>',
)

# ── HOW IT WORKS ─────────────────────────────────────────────────────────────

rep(
    '        <div class="section-tag">How It Works</div>',
    '        <div class="section-tag">{{ content.how_it_works.tag }}</div>',
)

rep(
    '<h2 class="section-title">Set up in minutes,<br>not weeks.</h2>',
    '<h2 class="section-title">{{ content.how_it_works.title | safe }}</h2>',
)

rep(
    'No IT department required. No professional services contract. Just your course content and a few clicks.',
    '{{ content.how_it_works.subtitle }}',
)

rep(
    '        <div class="steps">\n'
    '          <div class="step">\n'
    '            <div class="step-line"></div>\n'
    '            <div class="step-num-col"><div class="step-num">1</div></div>\n'
    '            <div class="step-content">\n'
    '              <div class="step-tag">Educators</div>\n'
    '              <h3>Connect your LMS</h3>\n'
    '              <p>Link LearnUps to Canvas or your preferred LMS via LTI in minutes. We walk you through every step.</p>\n'
    '            </div>\n'
    '          </div>\n'
    '          <div class="step">\n'
    '            <div class="step-line"></div>\n'
    '            <div class="step-num-col"><div class="step-num">2</div></div>\n'
    '            <div class="step-content">\n'
    '              <div class="step-tag">Educators</div>\n'
    '              <h3>Build or adopt your course</h3>\n'
    '              <p>Create your own questions or adopt OER content with ready-made assessments. Mix question types to deepen evaluation.</p>\n'
    '            </div>\n'
    '          </div>\n'
    '          <div class="step">\n'
    '            <div class="step-num-col"><div class="step-num">3</div></div>\n'
    '            <div class="step-content">\n'
    '              <div class="step-tag">Students</div>\n'
    '              <h3>Students learn, you see results</h3>\n'
    '              <p>Students access assignments through their existing LMS. Grades flow back automatically. You focus on teaching.</p>\n'
    '            </div>\n'
    '          </div>\n'
    '        </div>',
    '        <div class="steps">\n'
    '          {% for step in content.how_it_works.steps %}\n'
    '          <div class="step">\n'
    '            {% if not loop.last %}<div class="step-line"></div>{% endif %}\n'
    '            <div class="step-num-col"><div class="step-num">{{ loop.index }}</div></div>\n'
    '            <div class="step-content">\n'
    '              <div class="step-tag">{{ step.role_tag }}</div>\n'
    '              <h3>{{ step.title }}</h3>\n'
    '              <p>{{ step.desc }}</p>\n'
    '            </div>\n'
    '          </div>\n'
    '          {% endfor %}\n'
    '        </div>',
)

# ── AUDIENCE ─────────────────────────────────────────────────────────────────

rep(
    '      <div class="section-tag">Built for both sides of the classroom</div>',
    '      <div class="section-tag">{{ content.audience.tag }}</div>',
)

rep(
    '<h2 class="section-title">One platform, two experiences</h2>',
    '<h2 class="section-title">{{ content.audience.title }}</h2>',
)

# Educator card
rep(
    '        <div class="audience-label">For Educators</div>',
    '        <div class="audience-label">{{ content.audience.educator.label }}</div>',
)
rep(
    '        <h2>Design assessments that actually measure learning.</h2>',
    '        <h2>{{ content.audience.educator.title }}</h2>',
)
rep(
    '        <p>Stop recycling the same 10 questions. Use our question bank tools, OER integrations, and analytics to build richer, more effective homework experiences.</p>',
    '        <p>{{ content.audience.educator.desc }}</p>',
)

rep(
    '        <ul class="check-list">\n'
    '          <li><span class="check-icon">✓</span>Mix question types per learning outcome</li>\n'
    '          <li><span class="check-icon">✓</span>Connect to Canvas in under 5 minutes</li>\n'
    '          <li><span class="check-icon">✓</span>See per-question difficulty analytics</li>\n'
    '          <li><span class="check-icon">✓</span>Transfer grades to your LMS automatically</li>\n'
    '          <li><span class="check-icon">✓</span>OER course content adoption support</li>\n'
    '        </ul>\n'
    '        <div class="qt-pills">\n'
    '          <span class="qt-pill">Multiple Choice</span>\n'
    '          <span class="qt-pill">True / False</span>\n'
    '          <span class="qt-pill">Fill in the Blank</span>\n'
    '          <span class="qt-pill">Matching</span>\n'
    '          <span class="qt-pill">Short Answer</span>\n'
    '          <span class="qt-pill">Ordering</span>\n'
    '        </div>\n'
    '        <div style="margin-top: 1.75rem;">\n'
    '          <a href="#" class="btn-audience-ed">Request Instructor Account →</a>\n'
    '        </div>',
    '        <ul class="check-list">\n'
    '          {% for item in content.audience.educator.checklist %}\n'
    '          <li><span class="check-icon">✓</span>{{ item }}</li>\n'
    '          {% endfor %}\n'
    '        </ul>\n'
    '        <div class="qt-pills">\n'
    '          {% for pill in content.audience.educator.pills %}\n'
    '          <span class="qt-pill">{{ pill }}</span>\n'
    '          {% endfor %}\n'
    '        </div>\n'
    '        <div style="margin-top: 1.75rem;">\n'
    '          <a href="{{ content.audience.educator.btn_href }}" class="btn-audience-ed">{{ content.audience.educator.btn }}</a>\n'
    '        </div>',
)

# Student card
rep(
    '        <div class="audience-label">For Students</div>',
    '        <div class="audience-label">{{ content.audience.student.label }}</div>',
)
rep(
    '        <h2>Access homework anywhere, track your progress easily.</h2>',
    '        <h2>{{ content.audience.student.title }}</h2>',
)
rep(
    "        <p>Students access LearnUps through the same Canvas course they already use. No new accounts to create. No extra apps to install.</p>",
    "        <p>{{ content.audience.student.desc }}</p>",
)

rep(
    '        <ul class="check-list">\n'
    '          <li><span class="check-icon">✓</span>Access via your existing Canvas course</li>\n'
    '          <li><span class="check-icon">✓</span>Instant feedback on submissions</li>\n'
    '          <li><span class="check-icon">✓</span>Progress tracking across all assignments</li>\n'
    '          <li><span class="check-icon">✓</span>Grades appear in Canvas automatically</li>\n'
    '          <li><span class="check-icon">✓</span>Free for all students, always</li>\n'
    '        </ul>\n'
    '        <div style="margin-top: 2.5rem;">\n'
    '          <a href="#" class="btn-audience-st">Student Registration Guide →</a>\n'
    '        </div>',
    '        <ul class="check-list">\n'
    '          {% for item in content.audience.student.checklist %}\n'
    '          <li><span class="check-icon">✓</span>{{ item }}</li>\n'
    '          {% endfor %}\n'
    '        </ul>\n'
    '        <div style="margin-top: 2.5rem;">\n'
    '          <a href="{{ content.audience.student.btn_href }}" class="btn-audience-st">{{ content.audience.student.btn }}</a>\n'
    '        </div>',
)

# ── INTEGRATION ───────────────────────────────────────────────────────────────

rep(
    '  <h2>Plays nicely with your existing stack</h2>',
    '  <h2>{{ content.integration.title }}</h2>',
)

rep(
    '  <p>LearnUps integrates with any LTI-compatible LMS. Setup takes minutes, not days.</p>',
    '  <p>{{ content.integration.desc }}</p>',
)

rep(
    '  <div class="integration-badges">\n'
    '    <div class="int-badge"><span class="int-badge-dot"></span>LTI 1.3 Compatible</div>\n'
    '    <div class="int-badge"><span class="int-badge-dot"></span>Canvas LMS</div>\n'
    '    <div class="int-badge"><span class="int-badge-dot"></span>Grade Passback</div>\n'
    '    <div class="int-badge"><span class="int-badge-dot"></span>SSO Support</div>\n'
    '    <div class="int-badge"><span class="int-badge-dot"></span>FERPA Compliant</div>\n'
    '  </div>',
    '  <div class="integration-badges">\n'
    '    {% for badge in content.integration.badges %}\n'
    '    <div class="int-badge"><span class="int-badge-dot"></span>{{ badge }}</div>\n'
    '    {% endfor %}\n'
    '  </div>',
)

# ── PRICING ───────────────────────────────────────────────────────────────────

rep(
    '      <div class="section-tag">Simple Pricing</div>',
    '      <div class="section-tag">{{ content.pricing.tag }}</div>',
)

rep(
    '<h2 class="section-title">Priced for educators,<br>not enterprise.</h2>',
    '<h2 class="section-title">{{ content.pricing.title | safe }}</h2>',
)

rep(
    '      <p class="section-sub">No per-student fees. No hidden costs. Students always use LearnUps for free.</p>',
    '      <p class="section-sub">{{ content.pricing.subtitle }}</p>',
)

rep(
    '    <div class="pricing-grid">\n'
    '      <div class="pricing-card">\n'
    '        <div class="plan-label">Starter</div>\n'
    '        <div class="plan-name">Free</div>\n'
    '        <div class="plan-price">\n'
    '          <span class="amount">$0</span>\n'
    '          <span class="period">/ month</span>\n'
    '        </div>\n'
    '        <p class="plan-desc">Try LearnUps with one course. No credit card required.</p>\n'
    '        <hr class="divider-line" />\n'
    '        <ul class="plan-features">\n'
    '          <li>1 active course</li>\n'
    '          <li>Up to 50 students</li>\n'
    '          <li>All question types</li>\n'
    '          <li>LTI integration</li>\n'
    '          <li>Email support</li>\n'
    '        </ul>\n'
    '        <a href="#" class="btn-plan">Start Free</a>\n'
    '      </div>\n'
    '      <div class="pricing-card featured">\n'
    '        <div class="popular-badge">Most Popular</div>\n'
    '        <div class="plan-label">Instructor</div>\n'
    '        <div class="plan-name">Pro</div>\n'
    '        <div class="plan-price">\n'
    '          <span class="amount">$9</span>\n'
    '          <span class="period">/ month</span>\n'
    '        </div>\n'
    '        <p class="plan-desc">Full access for a single instructor. Unlimited courses and students.</p>\n'
    '        <hr class="divider-line" />\n'
    '        <ul class="plan-features">\n'
    '          <li>Unlimited courses</li>\n'
    '          <li>Unlimited students</li>\n'
    '          <li>All question types</li>\n'
    '          <li>Analytics dashboard</li>\n'
    '          <li>Grade passback</li>\n'
    '          <li>OER course adoption</li>\n'
    '          <li>Priority support</li>\n'
    '        </ul>\n'
    '        <a href="#" class="btn-plan-featured">Get Started</a>\n'
    '      </div>\n'
    '      <div class="pricing-card">\n'
    '        <div class="plan-label">Institution</div>\n'
    '        <div class="plan-name">Department</div>\n'
    '        <div class="plan-price">\n'
    '          <span class="amount">$49</span>\n'
    '          <span class="period">/ month</span>\n'
    '        </div>\n'
    '        <p class="plan-desc">For departments with multiple instructors who want a shared workspace.</p>\n'
    '        <hr class="divider-line" />\n'
    '        <ul class="plan-features">\n'
    '          <li>Up to 10 instructors</li>\n'
    '          <li>Shared question bank</li>\n'
    '          <li>Department analytics</li>\n'
    '          <li>Admin dashboard</li>\n'
    '          <li>Custom LTI setup</li>\n'
    '          <li>Dedicated onboarding</li>\n'
    '          <li>SLA support</li>\n'
    '        </ul>\n'
    '        <a href="#" class="btn-plan">Contact Sales</a>\n'
    '      </div>\n'
    '    </div>',
    '    <div class="pricing-grid">\n'
    '      {% for plan in content.pricing.plans %}\n'
    '      <div class="pricing-card{% if plan.highlighted %} featured{% endif %}">\n'
    '        {% if plan.popular_badge %}<div class="popular-badge">{{ plan.popular_badge }}</div>{% endif %}\n'
    '        <div class="plan-label">{{ plan.label }}</div>\n'
    '        <div class="plan-name">{{ plan.name }}</div>\n'
    '        <div class="plan-price">\n'
    '          <span class="amount">{{ plan.price }}</span>\n'
    '          <span class="period">{{ plan.period }}</span>\n'
    '        </div>\n'
    '        <p class="plan-desc">{{ plan.desc }}</p>\n'
    '        <hr class="divider-line" />\n'
    '        <ul class="plan-features">\n'
    '          {% for feature in plan.features %}\n'
    '          <li>{{ feature }}</li>\n'
    '          {% endfor %}\n'
    '        </ul>\n'
    '        <a href="{{ plan.btn_href }}" class="{% if plan.highlighted %}btn-plan-featured{% else %}btn-plan{% endif %}">{{ plan.btn }}</a>\n'
    '      </div>\n'
    '      {% endfor %}\n'
    '    </div>',
)

# ── TESTIMONIALS ──────────────────────────────────────────────────────────────

rep(
    '      <div class="section-tag">Testimonials</div>',
    '      <div class="section-tag">{{ content.testimonials.tag }}</div>',
)

rep(
    '<h2 class="section-title">Educators love it</h2>',
    '<h2 class="section-title">{{ content.testimonials.title }}</h2>',
)

# Build the exact testimonial grid from the original HTML
import re as _re
tgrid_match = _re.search(
    r'(<div class="testimonials-grid">.*?</div>\s*</div>\s*</section>)',
    html, _re.DOTALL
)
if tgrid_match:
    old_tgrid = tgrid_match.group(1)
    # Find just the testimonials-grid div content
    inner_match = _re.search(r'<div class="testimonials-grid">(.*?)</div>\s*</div>\s*</section>', html, _re.DOTALL)
    if inner_match:
        old_block = f'<div class="testimonials-grid">{inner_match.group(1)}</div>'
        new_block = (
            '    <div class="testimonials-grid">\n'
            '      {% for t in content.testimonials.items %}\n'
            '      <div class="testimonial">\n'
            '        <div class="stars">{{ t.stars }}</div>\n'
            '        <p class="quote">&ldquo;{{ t.quote }}&rdquo;</p>\n'
            '        <div class="testimonial-author">\n'
            '          <div class="avatar">{{ t.name[:2].upper() }}</div>\n'
            '          <div>\n'
            '            <div class="author-name">{{ t.name }}</div>\n'
            '            <div class="author-role">{{ t.role }}</div>\n'
            '          </div>\n'
            '        </div>\n'
            '      </div>\n'
            '      {% endfor %}\n'
            '    </div>'
        )
        rep(old_block, new_block)

# ── CTA BANNER ───────────────────────────────────────────────────────────────

rep(
    '    <h2>Ready to upgrade your homework system?</h2>',
    '    <h2>{{ content.cta.title }}</h2>',
)

rep(
    "    <p>Join thousands of educators who've switched to LearnUps. Free to start, no credit card needed.</p>",
    '    <p>{{ content.cta.subtitle }}</p>',
)

rep(
    '      <a href="#" class="btn-cta-dark">Start Your Free Trial</a>',
    '      <a href="{{ content.cta.btn_primary_href }}" class="btn-cta-dark">{{ content.cta.btn_primary }}</a>',
)

rep(
    '      <a href="#contact" class="btn-cta-outline">Talk to Our Team</a>',
    '      <a href="{{ content.cta.btn_secondary_href }}" class="btn-cta-outline">{{ content.cta.btn_secondary }}</a>',
)

# ── FOOTER ───────────────────────────────────────────────────────────────────

rep(
    '        <p>Low-cost online homework and assessment platform for educators who care about student outcomes.</p>',
    '        <p>{{ content.footer.desc }}</p>',
)

# Replace the Cloudflare-mangled email line
cf_email_pattern = _re.compile(
    r'<p style="margin-top: 8px;">Newark, CA · <a href="[^"]*" class="__cf_email__"[^>]*>\[email[^\]]*\]</a></p>'
)
html = cf_email_pattern.sub(
    '<p style="margin-top: 8px;">{{ content.footer.location }} · <a href="mailto:{{ content.footer.email }}">{{ content.footer.email }}</a></p>',
    html,
    count=1,
)

rep(
    '      <div class="footer-col">\n'
    '        <h4>Product</h4>\n'
    '        <ul>\n'
    '          <li><a href="#">Features</a></li>\n'
    '          <li><a href="#">Pricing</a></li>\n'
    '          <li><a href="#">Integrations</a></li>\n'
    '          <li><a href="#">Security</a></li>\n'
    '          <li><a href="#">Roadmap</a></li>\n'
    '        </ul>\n'
    '      </div>\n'
    '      <div class="footer-col">\n'
    '        <h4>Educators</h4>\n'
    '        <ul>\n'
    '          <li><a href="#">Getting Started</a></li>\n'
    '          <li><a href="#">Canvas LTI Guide</a></li>\n'
    '          <li><a href="#">OER Courses</a></li>\n'
    '          <li><a href="#">Question Types</a></li>\n'
    '          <li><a href="#">Analytics</a></li>\n'
    '        </ul>\n'
    '      </div>\n'
    '      <div class="footer-col">\n'
    '        <h4>Company</h4>\n'
    '        <ul>\n'
    '          <li><a href="#">About Us</a></li>\n'
    '          <li><a href="#">Blog</a></li>\n'
    '          <li><a href="#">Support</a></li>\n'
    '          <li><a href="#">Privacy Policy</a></li>\n'
    '          <li><a href="#">Terms of Service</a></li>\n'
    '        </ul>\n'
    '      </div>',
    '      {% for col in content.footer.columns %}\n'
    '      <div class="footer-col">\n'
    '        <h4>{{ col.title }}</h4>\n'
    '        <ul>\n'
    '          {% for link in col.links %}\n'
    '          <li><a href="{{ link.href }}">{{ link.text }}</a></li>\n'
    '          {% endfor %}\n'
    '        </ul>\n'
    '      </div>\n'
    '      {% endfor %}',
)

rep(
    '© 2025 LearnUps / EdTechs. All rights reserved.',
    '{{ content.footer.copyright }}',
)

# ── WRITE OUTPUT ─────────────────────────────────────────────────────────────

if warns:
    print("WARNINGS:")
    for w in warns:
        print(w)

with open(DST, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n✓ Template written to {DST}  ({len(html):,} bytes)")
