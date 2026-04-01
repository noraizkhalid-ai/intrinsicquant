import os, re

files = ['index.html', 'about/index.html', 'contact/index.html']

for f in files:
    path = os.path.join('/Users/noraiz/Work/sites/IntrinsicQuant', f)
    if not os.path.exists(path):
        continue
    with open(path, 'r') as file:
        html = file.read()
        
    # --- FOOTER QUICK LINKS ---
    old_footer_links = r'<li><a href="/hr-services/">Human Resources \(HR\)</a></li>\s*<li><a href="/financial-services/">Finance</a></li>\s*<li><a href="/it-services/">Information Technology \(IT\)</a></li>\s*<li><a href="/branding-services/">Branding & Creative</a></li>'
    new_footer_links = '''<li><a href="/#services">Quantitative Terminal</a></li>
            <li><a href="/#services">Fundamentals API</a></li>
            <li><a href="/#services">Options Flow</a></li>
            <li><a href="/#services">Alternative Data</a></li>'''
    html = re.sub(old_footer_links, new_footer_links, html, flags=re.DOTALL)
    
    # Update Footer "Affordable. Reliable. Professional."
    html = html.replace("Affordable. Reliable. Professional.", "Institutional. Accurate. Accessible.")
    
    # --- LOGO PATHS ---
    html = html.replace('src="../assets/images/Png Logo.png"', 'src="/assets/images/logo.png"')
    html = html.replace('src="../assets/images/Png%20Logo.png"', 'src="/assets/images/logo.png"')
    html = html.replace('src="/assets/images/Png Logo.png"', 'src="/assets/images/logo.png"')
    html = html.replace('src="/assets/images/Png%20Logo.png"', 'src="/assets/images/logo.png"')
    
    # --- ABOUT PAGE SPECIFIC FIXES ---
    if 'about' in f:
        html = re.sub(
            r'Most small businesses in Pakistan.*?price that actually makes sense\.',
            "For decades, the highest quality financial datasets and fundamental models were locked behind $25k-a-year terminals. We built IntrinsicQuant to break that monopoly, providing systematic traders and researchers with absolute data integrity at an accessible price.",
            html,
            flags=re.DOTALL
        )
        html = re.sub(
            r'Core Bhive was founded in 2025 in Lahore.*?small and medium business in Pakistan\.',
            "IntrinsicQuant was founded to deliver uncompromised point-in-time financial data, options flow analytics, and systematic signals to traders everywhere.",
            html,
            flags=re.DOTALL
        )
        html = re.sub(
            r'For too long, quality outsourcing has been reserved.*?actually running their business\.',
            "Legacy data providers routinely fail to adjust for survivorship bias or corporate restructurings, leading to catastrophic backtest errors.",
            html,
            flags=re.DOTALL
        )
        html = re.sub(
            r'We built Core Bhive as a subscription-based outsourcing partner.*?cost to hire internally\.',
            "We built IntrinsicQuant's proprietary ingestion engine to cross-reference every SEC filing, ensuring our fundamental data feeds are mechanically flawless.",
            html,
            flags=re.DOTALL
        )
        html = re.sub(
            r'Based in DHA Phase 6 Lahore.*?Pakistani market\.',
            "Our team consists of former quantitative researchers, data engineers, and market practitioners who understand that in systematic trading, your edge is only as derived as your data.",
            html,
            flags=re.DOTALL
        )
        
        # CTAs
        html = html.replace('Book a Free Meeting', 'Request Trial Access')
        html = html.replace('Book a free 30-minute consultation. No commitment.', 'Request access to our API endpoints or schedule a live terminal demonstration.')
        html = html.replace('Ready to hand off the work that\'s holding you back?', 'Ready to build your quantitative edge?')

    with open(path, 'w') as file:
        file.write(html)

print("Final Polish Applied")
