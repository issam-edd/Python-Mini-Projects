from PIL import Image, ImageFilter

img = Image.open('./finalgig1.jpg')

#new_img = img.resize((400, 400)) #RESIZE IS KILL THE QUALITY
img.thumbnail((1280, 769))
img.save('finalgig11.jpg')