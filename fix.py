import os, glob

files = ['index.html', 'about/index.html', 'contact/index.html']

for f in files:
    path = os.path.join('/Users/noraiz/Work/sites/IntrinsicQuant', f)
    if not os.path.exists(path):
        continue
    with open(path, 'r') as file:
        content = file.read()
    
    # Replace the exact gold hex color with the new cyan hex color
    content = content.replace('#FFB400', '#00E5FF')
    # Or lowercase just in case
    content = content.replace('#ffb400', '#00E5FF')
    
    # Update dead service links to point to the booking CTA which is #book or /contact/
    content = content.replace('href="/hr-services/"', 'href="/#book"')
    content = content.replace('href="/financial-services/"', 'href="/#book"')
    content = content.replace('href="/it-services/"', 'href="/#book"')
    content = content.replace('href="/branding-services/"', 'href="/#book"')
    
    with open(path, 'w') as file:
        file.write(content)

print("Icons and broken links fixed.")
