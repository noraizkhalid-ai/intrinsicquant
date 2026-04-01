import os, re

files = ['index.html', 'about/index.html', 'contact/index.html']

for file in files:
    path = os.path.join('/Users/noraiz/Work/sites/IntrinsicQuant', file)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r') as f:
        content = f.read()

    # Update Title
    if 'index.html' == file:
        content = re.sub(r'<title>.*?</title>', '<title>IntrinsicQuant — Quantitative Financial Intelligence</title>', content)
        desc = "IntrinsicQuant is a Bloomberg-grade quantitative data platform delivering point-in-time fundamentals, options flow, and API access to systematic traders."
    elif 'about' in file:
        content = re.sub(r'<title>.*?</title>', '<title>About Us — IntrinsicQuant</title>', content)
        desc = "Learn about IntrinsicQuant and our mission to democratize institutional-grade financial data."
    else:
        content = re.sub(r'<title>.*?</title>', '<title>Contact — IntrinsicQuant</title>', content)
        desc = "Contact IntrinsicQuant for API trial access, Enterprise Snowflake delivery, or General support."

    # Update Meta Description
    content = re.sub(
        r'<meta name="description"\s*content=".*?">',
        f'<meta name="description"\n    content="{desc}">',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<meta property="og:description"\s*content=".*?">',
        f'<meta property="og:description"\n    content="{desc}">',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<meta name="twitter:description"\s*content=".*?">',
        f'<meta name="twitter:description" content="{desc}">',
        content,
        flags=re.DOTALL
    )
    
    with open(path, 'w') as f:
        f.write(content)

print("SEO update complete.")
