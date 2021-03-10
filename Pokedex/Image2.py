from PIL import Image

img = Image.open('pikachu.jpg')
filtered_img = img.convert('L')
resize = filtered_img.resize((300, 300))
resize.save('resize.png', 'png')



