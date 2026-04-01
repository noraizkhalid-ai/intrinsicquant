import os, re

about_path = '/Users/noraiz/Work/sites/IntrinsicQuant/about/index.html'
contact_path = '/Users/noraiz/Work/sites/IntrinsicQuant/contact/index.html'

# === ABOUT PAGE ===
if os.path.exists(about_path):
    with open(about_path, 'r') as f:
        html = f.read()
        
    # Hero
    html = html.replace("We Exist Because Pakistani Businesses Deserve Better.", "Democratizing Institutional-Grade Financial Intelligence.")
    html = html.replace(
        "Most small businesses in Pakistan can't afford a full-time HR manager,\n          accountant, or IT team. We built Core Bhive to change that — giving every SME access to professional\n          operational support at a price that actually makes sense.",
        "For decades, the highest quality financial datasets and fundamental models were locked behind $25k-a-year terminals. We built IntrinsicQuant to break that monopoly, providing systematic traders and researchers with absolute data integrity at an accessible price."
    )
    
    # Story
    html = html.replace(
        "We saw small businesses struggling with problems that had simple solutions. So we built them.",
        "We saw quantitative researchers struggling with fragmented, biased, and noisy data. So we cleaned it up."
    )
    html = html.replace(
        "Core Bhive was founded in 2025 in Lahore with a straightforward mission — make professional HR, finance,\n            and IT support accessible to every small and medium business in Pakistan.",
        "IntrinsicQuant was founded to deliver uncompromised point-in-time financial data, options flow analytics, and systematic signals to traders everywhere."
    )
    html = html.replace(
        "For too long, quality outsourcing has been reserved for large corporations with big budgets. Small business\n            owners were left juggling payroll, chasing invoices, fixing WiFi, and recruiting staff — all on top of\n            actually running their business.",
        "Legacy data providers routinely fail to adjust for survivorship bias or corporate restructurings, leading to catastrophic backtest errors."
    )
    html = html.replace(
        "We built Core Bhive as a subscription-based outsourcing partner that works exactly like an in-house team,\n            without the overhead. Our clients get dedicated professionals, monthly deliverables, and a single point of\n            contact — at a fraction of what it would cost to hire internally.",
        "We built IntrinsicQuant's proprietary ingestion engine to cross-reference every SEC filing, ensuring our fundamental data feeds are mechanically flawless."
    )
    html = html.replace(
        "Based in DHA Phase 6 Lahore, we work with businesses across the city and understand the specific challenges\n            of operating in the Pakistani market.",
        "Our team consists of former quantitative researchers, data engineers, and market practitioners who understand that in systematic trading, your edge is only as derived as your data."
    )
    
    # Mission
    html = html.replace(
        "To deliver affordable, reliable, and professional HR, financial, and IT outsourcing solutions that help\n            small and medium businesses in Pakistan operate efficiently and grow sustainably.",
        "To provide the world's most pristine structured financial datasets and terminal analytics, empowering algorithmic researchers with institutional-grade edge."
    )
    html = html.replace(
        "To become Pakistan's leading business outsourcing brand — where companies confidently delegate their\n            operations knowing they have a trusted long-term partner behind them.",
        "To become the central nervous system for quantitative market research worldwide."
    )
    
    # Differences
    html = html.replace("Not an agency. <span class=\"italic-accent\">A partner.</span>", "Not just data. <span class=\"italic-accent\">Intelligence.</span>")
    html = html.replace("Affordable by Design", "Accessible by Design")
    html = html.replace(
        "We built our pricing model around what Pakistani SMEs can actually afford — not what the market typically\n            charges.",
        "We structure our pricing so boutiques, independent researchers, and hedge funds alike can power their strategies without predatory terminal fees."
    )
    html = html.replace("Local and On the Ground", "Point-in-Time Perfect")
    html = html.replace(
        "We are based in Lahore, we understand local business culture, local compliance, and the specific challenges\n            of operating here.",
        "We strictly eliminate look-ahead and survivorship bias out of all historical metrics to ensure backtests hold up in live trading environments."
    )
    html = html.replace("One Point of Contact", "Zero Black Boxes")
    html = html.replace(
        "No call centres, no ticketing systems. You have one dedicated person who knows your business inside out and\n            is always reachable.",
        "We believe in mathematical transparency. All custom factors, scoring rubrics, and quant screens are fully documented."
    )
    
    # Values
    html = html.replace("Affordable", "Accessible")
    html = html.replace("Quality support should not be a privilege reserved for big companies.", "Data dominance shouldn't be locked behind legacy terminals.")
    html = html.replace("Reliable", "Unyielding Accuracy")
    html = html.replace("You should never have to chase us. Deliverables arrive on time, every time.", "Garbage in, garbage out. We cross-verify everything.")
    html = html.replace("Professional", "Institutional Depth")
    html = html.replace("Every output we deliver reflects the same standard you would expect from an enterprise team.", "Our feature sets parallel Bloomberg, Capital IQ, and Refinitiv tools.")
    
    # SEO
    html = html.replace("<title>About Us — Core Bhive</title>", "<title>About Us — IntrinsicQuant Data Terminal</title>")

    with open(about_path, 'w') as f:
        f.write(html)

# === CONTACT PAGE ===
if os.path.exists(contact_path):
    with open(contact_path, 'r') as f:
        html = f.read()
        
    html = html.replace("<title>Contact Us — Core Bhive</title>", "<title>Contact Us — IntrinsicQuant</title>")
    html = html.replace(
        "Book a free 30-minute consultation or send us a message — we respond within 2 hours.",
        "Request API trial keys, inquire about enterprise data feeds, or schedule a live Terminal walkthrough."
    )
    
    # Update Form dropdowns
    pattern_services = r'<option value="HR Services — Recruitment & Hiring">.*?</option>\s*.*?<option value="Not Sure — I Need Advice">Not Sure — I Need Advice</option>'
    
    new_services = '''<option value="Professional Subscription Trial">Professional Subscription Trial</option>
                  <option value="Institutional Tier Evaluation">Institutional Tier Evaluation</option>
                  <option value="Enterprise REST API Sandbox">Enterprise REST API Sandbox</option>
                  <option value="Snowflake Data Sharing (Enterprise)">Snowflake Data Sharing (Enterprise)</option>
                  <option value="General Support/Inquiry">General Support/Inquiry</option>'''
                  
    html = re.sub(pattern_services, new_services, html, flags=re.DOTALL)
    
    # Replace Logo links (if not already done by previous script, but good measure)
    html = html.replace("assets/images/Png Logo.png", "assets/images/logo.png")
    html = html.replace("assets/images/Png%20Logo.png", "assets/images/logo.png")

    with open(contact_path, 'w') as f:
        f.write(html)

print("About and Contact pages overhauled.")
