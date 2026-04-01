import os, re

# 1. Clean contact/index.html
contact_path = '/Users/noraiz/Work/sites/IntrinsicQuant/contact/index.html'
if os.path.exists(contact_path):
    with open(contact_path, 'r') as f:
        content = f.read()

    # Remove WhatsApp mention in form text
    content = content.replace('We have received your message and will WhatsApp or email you within 2 hours.', 'We have received your message and will email you within 2 hours.')
    content = content.replace('We will WhatsApp you on this number.', 'We will contact you on this number.')
    
    # Remove WhatsApp option
    content = re.sub(r'<option value="WhatsApp">WhatsApp</option>\s*', '', content)
    
    # Remove LinkedIn option
    content = re.sub(r'<option value="LinkedIn">LinkedIn</option>\s*', '', content)

    # Remove WhatsApp Block
    content = re.sub(
        r'<!-- Block 1: WhatsApp -->.*?<!-- Block 2: Email -->',
        r'<!-- Block 2: Email -->',
        content,
        flags=re.DOTALL
    )
    
    # Remove contact-cta__headline mentioning WhatsApp
    content = re.sub(
        r'<h2 class="contact-cta__headline">WhatsApp us right now and get a response within 2 hours\.</h2>',
        r'<h2 class="contact-cta__headline">Email us right now and get a response within 2 hours.</h2>',
        content
    )

    # Remove LinkedIn block
    content = re.sub(
        r'<!-- Block 5: LinkedIn -->.*?(?=</div>\s*</div>\s*<!-- ═══════════════════════════════════════════)',
        r'',
        content,
        flags=re.DOTALL
    )

    with open(contact_path, 'w') as f:
        f.write(content)

# 2. Clean main.js
js_path = '/Users/noraiz/Work/sites/IntrinsicQuant/js/main.js'
if os.path.exists(js_path):
    with open(js_path, 'r') as f:
        content = f.read()
    
    # Remove floating WhatsApp button
    content = re.sub(
        r'/\*\s*── FLOATING WHATSAPP BUTTON ──\s*\*/.*?document\.body\.appendChild\(waBtn\);',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(js_path, 'w') as f:
        f.write(content)

print("Remaining cleanups successful.")
