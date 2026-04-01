import os

files = ['index.html', 'about/index.html', 'contact/index.html']

for file in files:
    path = os.path.join('/Users/noraiz/Work/sites/IntrinsicQuant', file)
    if not os.path.exists(path):
        continue
    with open(path, 'r') as f:
        html = f.read()
    
    html = html.replace('height="44"', 'height="80"')
    
    with open(path, 'w') as f:
        f.write(html)
        
print("HTML updated.")
