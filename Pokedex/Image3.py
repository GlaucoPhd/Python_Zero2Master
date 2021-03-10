from PIL import Image

img = Image.open('pikachu.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('grey.png', 'png')
