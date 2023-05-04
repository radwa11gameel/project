# from PIL import Image, ImageDraw
# /Users/AhmedS/Desktop/DEV/Django/core-master/mypro/mypic.jpeg

from PIL import Image, ImageOps

# open the image file
img = Image.open('mypro/radwa2.jpeg')

# convert the image to grayscale
img = ImageOps.grayscale(img)

# posterize the image to reduce the number of colors
img = ImageOps.posterize(img, 2)
img = img.resize((120, 110))
# get the ASCII characters corresponding to each pixel
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
ascii_pixels = [ascii_chars[pixel//25] for pixel in img.getdata()]

# group the ASCII characters into rows and print them
width, height = img.size
ascii_rows = ["".join(ascii_pixels[x:x+width]) for x in range(0, len(ascii_pixels), width)]
print("\n".join(ascii_rows))
