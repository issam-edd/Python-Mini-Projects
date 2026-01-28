from PIL import Image, ImageFilter
img = Image.open('./Pokedex/4.4 pikachu.jpg')
# filtred_img = img.filter(ImageFilter.SHARPEN)
filtred_img = img.convert('L')
crooked = filtred_img.rotate(180)
crooked.save("Pgray.png", 'png')
# filtred_img.save("Pgray.png", 'png')
crooked.show(img)