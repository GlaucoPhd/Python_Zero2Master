# File is to big
# print(img.size) = (5611, 5339)
# When we want to keep the scale without squeeze
# thumbnail keep the aspect decide the best size to the image
from PIL import Image

img = Image.open('astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)


