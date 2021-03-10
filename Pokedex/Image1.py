# Convert the file to one object that we can manipulate
# PIL image show up all the atributes of the image
# Create a new file
from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("blur.png", "png")

# Convert image format

img_black_white = Image.open('pikachu.jpg')
filtered_img = img_black_white.convert('L')

filtered_img.save("gray.png", "png")