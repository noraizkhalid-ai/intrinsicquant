import os, re

files = ['index.html', 'about/index.html', 'contact/index.html']

for file in files:
    filepath = os.path.join('/Users/noraiz/Work/sites/IntrinsicQuant', file)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()
        
    # 1. Update Services link in nav and remove dropdown
    content = re.sub(
        r'<a href="/#services" class="nav__link nav__link--parent">Services</a>\s*<ul class="nav__dropdown">.*?</ul>',
        r'<a href="/#services" class="nav__link">Services</a>',
        content,
        flags=re.DOTALL
    )
    
    # 2. Remove insights from nav
    content = re.sub(
        r'<li class="nav__item">\s*<a href="/blog/" class="nav__link">Insights</a>\s*</li>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 3. Remove WhatsApp from nav__ctas
    content = re.sub(
        r'<a class="btn btn--sm btn--secondary" href="https://wa\.me/[^>]+>.*?WhatsApp\s*</a>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 4. Simplify mobile nav Services
    content = re.sub(
        r'<div class="nav__mobile-group">\s*<span class="nav__mobile-label">Services</span>\s*<div class="nav__mobile-sub">.*?</div>\s*</div>',
        r'<a href="/#services" class="nav__link">Services</a>',
        content,
        flags=re.DOTALL
    )
    
    # 5. Remove insights from mobile nav
    content = content.replace('<a href="/blog/" class="nav__link">Insights</a>', '')
    
    # 6. Remove WhatsApp from mobile nav
    content = re.sub(
        r'<a class="btn btn--secondary" href="https://wa\.me/[^>]+>WhatsApp\s*Us</a>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 7. Remove WhatsApp Us buttons globally
    content = re.sub(
        r'<a [^>]*href="https://wa\.me/[^>]+>[^<]*WhatsApp[^<]*</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    content = re.sub(
        r'<a [^>]*href="https://wa\.me/[^>]+>[^<]*<svg[^>]*>.*?</svg>[^<]*WhatsApp[^<]*</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    content = re.sub(
        r'<a class="footer-contact-link" href="https://wa\.me/[^>]+>[^<]*<svg[^>]*>.*?</svg>.*?</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # 8. Footer edits
    content = content.replace("Core B'hive", "IntrinsicQuant")
    content = content.replace("Core Bhive", "IntrinsicQuant")
    # Remove insights from footer links
    content = re.sub(r'<li><a href="/blog/">Insights</a></li>\s*', '', content)
    # Remove footer-linkedin and footer-instagram links
    content = re.sub(
        r'<a class="footer-linkedin"[^>]*>.*?</a>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<a class="footer-linkedin"[^>]*>.*?</a>', # do it twice just in case regex doesn't catch both if they are adjacent or something? No wait, DOTALL with non-greedy catches each.
        '',
        content,
        flags=re.DOTALL
    )
    
    # 9. Remove vision behind section in about/index.html
    if file == 'about/index.html':
        content = re.sub(
            r'<!-- SECTION 7: FOUNDER -->.*?<!-- SECTION 8: CTA -->',
            r'<!-- SECTION 8: CTA -->',
            content,
            flags=re.DOTALL
        )
        
    with open(filepath, 'w') as f:
        f.write(content)

print("Done replacements")
