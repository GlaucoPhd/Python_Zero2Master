# Sys grab 1 and 2 argument
# Check new exists, if not create
# Loop all Pokedex and convert to PNG and save in a new folder
# pathlib or os module also to grab

import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')

print('All Done!')