import os
from PIL import Image
import bs4

os.system('cls')
mac = Image.open('.//Images//example.jpg')
# print(mac)
# print(mac.show())  # If JN then only mac will work
print(mac.size)
# print(mac.filename)
# print(mac.format_description)

# Fetch Mac Half
x = 800
y = 800
w = 1200
h = 1257
# print(w)
# print(mac.crop((x, y, w, h)).show())
mac_crop = mac.crop((x, y, w, h))
# print(mac_crop)
# print(mac.paste(im=mac_crop, box=(0, 0)))  # Just affecting the variable
# print(mac.show())
# mac.save('.//Images//mac_crop_out.jpg')
# print(mac.resize((100, 100)).show())  # Resize an Image
# print(mac.rotate(180).show())  # Rotate an Image

# exit()
pencils = Image.open('.//Images//pencils.jpg')
# print(pencil.show())
# print(pencil.size[0]) # Original Width
# print(pencil.size[1]) # Original Hight

# Fetch Top Pencils
x = 0
y = 0
w = (pencils.size[0])/3
h = (pencils.size[1])/8.7
# left, upper, right, and lower pixel coordinate
# print(pencils.crop((x, y, w, h)).show())

# Fetch Bottom Pencils
x = 0
y = 1100
w = (pencils.size[0])/3
h = 1300
# print(pencils.crop((x, y, w, h)).show())

# Color Transparency # RGBA - Red, Green, Blue, and Alpha
# Alpha - 0 (Transparent), 255 (Opaque)

red = Image.open('.//Images//red_color.jpg')
red.putalpha(128)
# print(red.show())

blue = Image.open('.//Images//blue_color.png')
blue.putalpha(254)
# print(blue.show())

# Generate Purple
blue.paste(im=red, box=(0, 0), mask=red)
# print(blue.show())
