from PIL import Image, ImageDraw

def create_icon(size, filename):
    img = Image.new('RGBA', (size, size), (102, 126, 234, 255))
    draw = ImageDraw.Draw(img)
    
    box_size = int(size * 0.6)
    offset = (size - box_size) // 2
    draw.rectangle([offset, offset, offset + box_size, offset + box_size], fill=(255, 255, 255, 255))
    
    draw.text((size//2, size//2), "📦", anchor="mm")
    
    img.save(filename, 'PNG')

create_icon(192, 'icon-192.png')
create_icon(512, 'icon-512.png')
print("Iconos creados: icon-192.png, icon-512.png")
