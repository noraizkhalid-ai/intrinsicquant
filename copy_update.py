import os, re

index_path = '/Users/noraiz/Work/sites/IntrinsicQuant/index.html'

with open(index_path, 'r') as f:
    html = f.read()

# --- HERO SECTION ---
html = html.replace("Pakistan's Business Outsourcing Partner", "Institutional-Grade Quantitative Intelligence")

headline_old = r'<h1 class="home-hero__headline">.*?</h1>'
headline_new = """<h1 class="home-hero__headline">
        <span class="word" style="animation-delay:0.10s">Outsmart</span>
        <span class="word" style="animation-delay:0.22s">The</span>
        <span class="word" style="animation-delay:0.34s">Market</span><br>
        <span class="word" style="animation-delay:0.50s">With</span>
        <span class="word" style="animation-delay:0.62s">Absolute</span>
        <span class="word" style="animation-delay:0.74s">Data</span>
        <span class="word" style="animation-delay:0.86s">Precision.</span>
      </h1>"""
html = re.sub(headline_old, headline_new, html, flags=re.DOTALL)

html = html.replace(
    "Outsourced HR, Finance, IT, and Branding services built for businesses across Pakistan.",
    "Advanced quantitative modeling, fundamental data feeds, and institutional insights built for systematic investors and asset managers."
)
html = html.replace("Book a Free Meeting", "Request Trial Access")

# --- CREDIBILITY STRIP ---
strip_old = r'<div class="cred-strip__track">.*?</div>\s*</div>'
strip_items = """
        <span>Quantitative Research</span><span class="diamond">◆</span>
        <span>Machine Learning Models</span><span class="diamond">◆</span>
        <span>Alternative Data</span><span class="diamond">◆</span>
        <span>Options Order Flow</span><span class="diamond">◆</span>
        <span>Fundamental Screening</span><span class="diamond">◆</span>
        <span>Real-Time API Feeds</span><span class="diamond">◆</span>
        <span>Risk Metrics</span><span class="diamond">◆</span>
"""
strip_new = f"""<div class="cred-strip__track">
      <p class="cred-strip__text">{strip_items}</p>
      <p class="cred-strip__text" aria-hidden="true">{strip_items}</p>
    </div>
  </div>"""
html = re.sub(strip_old, strip_new, html, flags=re.DOTALL)

# --- THE PROBLEM ---
html = html.replace('The Problem', 'The Edge')
html = html.replace("You didn't start a business to manage paperwork.", "An information advantage is a prerequisite.")
html = html.replace(
    "Most SME owners waste 30% of their week on HR, finance, IT, and branding\n        problems that should never reach their desk.",
    "In modern quantitative trading, navigating market noise without clean, point-in-time structured data means you are the liquidity for those who have it."
)

html = html.replace("Hiring the Wrong People", "Fragmented Data Sources")
html = html.replace("Every bad hire costs you time, money, and momentum you can't afford to lose.", "Piecing together fundamental data from scattered legacy vendors introduces unacceptable latency and normalization error.")

html = html.replace("Payroll Errors Damage Trust", "Look-Ahead Bias")
html = html.replace("Mistakes in payroll damage employee morale and expose you to costly compliance risk.", "Using non-point-in-time data guarantees your backtests will hallucinate returns that disappear in live markets.")

html = html.replace("IT Failures Kill Productivity", "Inflexible Delivery")
html = html.replace("When systems go down and there's no one to call, your whole business grinds to a halt.", "Tied to legacy terminals instead of having robust REST APIs or Snowflake delivery limits your systematic pipeline.")

html = html.replace("Your Brand Looks Unprofessional", "Black-Box Methodologies")
html = html.replace("Poor branding and inactive social media make potential clients choose competitors who simply look more credible.", "Relying on opaque third-party sentiment scores without access to the underlying calculations creates catastrophic blind spots.")

# --- SERVICES ---
html = html.replace("What We Do", "Our Platform")
html = html.replace("Everything your business needs.<br>Nothing it doesn't.", "Institutional-grade tools.<br>Delivered via modern architecture.")

# Card 1
html = html.replace("Human Resources (HR)", "Quantitative Analytics Terminal")
html = html.replace("From recruitment to payroll, fully managed.", "Access deep fundamental analysis, relative valuations, and custom factor models directly in your browser.")
# Card 2
html = html.replace("Finance", "Point-in-Time Fundamentals API")
html = html.replace("Bookkeeping, reporting, and budgeting done right.", "Over 20 years of point-in-time history, perfectly stitched to prevent survivorship bias in your backtesting.")
# Card 3
html = html.replace("Information Technology (IT)", "Options Flow & Positioning")
html = html.replace("Setup, support, and security for your office.", "Track institutional sweepers, block trades, and dealer gamma positioning to anticipate mechanical market movements.")
# Card 4
html = html.replace("Branding & Creative", "Alternative Data Integration")
html = html.replace("Logo design, graphic design, and social media management that makes your business look as good as it is.", "Credit card consensus, satellite imagery estimations, and social sentiment models quantified into actionable signals.")

# --- WHY US ---
html = html.replace("Why Us", "The IntrinsicQuant Advantage")
html = html.replace("Built differently.<br>On purpose.", "Engineering meets absolute accuracy.")

html = html.replace("Affordable Pricing", "Absolute Data Integrity")
html = html.replace("Expert-level support at SME-friendly rates — no enterprise markup.", "Every data point is strictly audited and cross-referenced. If we don't trust it with our own capital, it's not on the platform.")
html = html.replace("Local Expertise", "Sub-Millisecond APIs")
html = html.replace("We understand the Pakistani business landscape: taxes, culture, and compliance.", "Modern infrastructure built for quants. Access data via REST API, WebSockets, or direct Snowflake data shares.")
html = html.replace("No Lock-in", "Transparent Calculation")
html = html.replace("Month-to-month engagement. Cancel anytime — no penalties, no fine print.", "Open-book methodology on all custom factors and scoring models. Verify the math yourself before implementing.")
html = html.replace("Dedicated Support", "Institutional Coverage")
html = html.replace("One point of contact, always reachable — not a rotating support queue.", "Coverage of over 10,000+ global equities, fixed income derivatives, and macroeconomic indicators.")

# --- HOW IT WORKS (Change to PRICING) ---
html = html.replace("The Process", "Subscriptions")
html = html.replace("Up and running in days.", "Pricing Plans")

steps_old = r'<div class="steps-row">.*?</div>\s*</div>\s*</section>'
steps_new = """<div class="why-cols" style="margin-top:72px;">
        <div class="why-col" style="background:var(--color-black); border:1px solid var(--border-default); padding:40px 30px; border-radius:var(--radius-lg);">
          <h4 style="color:var(--color-gold); font-size:1.5rem;">Professional</h4>
          <p style="font-size:2rem; color:#fff; font-weight:700; margin: 15px 0;">$99<span style="font-size:1rem;color:grey;">/mo</span></p>
          <p style="margin-bottom:30px;">For sophisticated retail traders and independent analysts.</p>
          <ul style="color:rgba(240, 237, 230, 0.6); list-style:none; padding:0; display:flex; flex-direction:column; gap:12px; margin-bottom:40px;">
            <li>✓ Full Web Terminal Access</li>
            <li>✓ 10 Years Historical Data</li>
            <li>✓ Daily Options Flow Setup</li>
            <li>✓ Limited API Access (1K req/day)</li>
          </ul>
          <a href="/contact/" class="btn btn--secondary btn--full">Start 14-Day Trial</a>
        </div>
        
        <div class="why-col" style="background:linear-gradient(135deg, var(--color-black), #0a192f); border:1px solid var(--color-gold); padding:40px 30px; border-radius:var(--radius-lg); transform:scale(1.05); z-index:10; box-shadow:var(--shadow-gold);">
          <h4 style="color:var(--color-gold); font-size:1.5rem;">Institutional</h4>
          <p style="font-size:2rem; color:#fff; font-weight:700; margin: 15px 0;">$499<span style="font-size:1rem;color:grey;">/mo</span></p>
          <p style="margin-bottom:30px;">For systematic traders and boutique fund managers.</p>
          <ul style="color:rgba(240, 237, 230, 0.8); list-style:none; padding:0; display:flex; flex-direction:column; gap:12px; margin-bottom:40px;">
            <li>✓ Everything in Professional</li>
            <li>✓ 30+ Years Point-In-Time History</li>
            <li>✓ Real-Time Institutional Options Flow</li>
            <li>✓ Unlimited REST API & WebSockets</li>
            <li>✓ Alternative Data Supplements</li>
          </ul>
          <a href="/contact/" class="btn btn--primary btn--full">Upgrade to Institutional</a>
        </div>
        
        <div class="why-col" style="background:var(--color-black); border:1px solid var(--border-default); padding:40px 30px; border-radius:var(--radius-lg);">
          <h4 style="color:#fff; font-size:1.5rem;">Enterprise</h4>
          <p style="font-size:2rem; color:#fff; font-weight:700; margin: 15px 0;">Custom</p>
          <p style="margin-bottom:30px;">For asset managers requiring bulk data delivery.</p>
          <ul style="color:rgba(240, 237, 230, 0.6); list-style:none; padding:0; display:flex; flex-direction:column; gap:12px; margin-bottom:40px;">
            <li>✓ Direct Snowflake Sharing</li>
            <li>✓ AWS S3 Raw Data Dumps</li>
            <li>✓ Custom Quantitative Factor Modeling</li>
            <li>✓ Dedicated Solution Architect</li>
          </ul>
          <a href="/contact/" class="btn btn--ghost btn--full">Contact Sales</a>
        </div>
      </div>
    </div>
  </section>"""

html = re.sub(steps_old, steps_new, html, flags=re.DOTALL)

# --- CTA ---
html = html.replace("Ready to hand off the work that's holding you back?", "Ready to build your quantitative edge?")
html = html.replace("Book a free 30-minute consultation. No commitment.", "Request access to our API endpoints or schedule a live terminal demonstration.")
html = html.replace("Book a Meeting", "Request Access")

# Replace Logo links
html = html.replace("assets/images/Png Logo.png", "assets/images/logo.png")
html = html.replace("assets/images/Png%20Logo.png", "assets/images/logo.png")

with open(index_path, 'w') as f:
    f.write(html)
    
print("index.html successfully upgraded.")
