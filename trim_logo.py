from PIL import Image

def make_transparent_and_trim(image_path):
    # Open image and ensure RGBA mode
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    datas = img.getdata()
    new_data = []
    
    # Catch pure white and very light off-whites
    threshold = 240
    for item in datas:
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            # Replace white with transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    # getbbox() finds the bounding box of the non-zero (non-transparent) regions
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(image_path, "PNG")

if __name__ == "__main__":
    logo_path = '/Users/noraiz/Work/sites/IntrinsicQuant/assets/images/logo.png'
    make_transparent_and_trim(logo_path)
    print("Logo background removed and trimmed successfully.")
