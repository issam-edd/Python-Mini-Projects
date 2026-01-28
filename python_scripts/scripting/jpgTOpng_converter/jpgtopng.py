import re
import sys
import os
from PIL import Image
image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cmpt = 0
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    cmpt += 1

if cmpt > 0:
    print('all done!')
else:
    raise 'erorr'




