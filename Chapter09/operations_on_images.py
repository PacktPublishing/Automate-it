#Paste image on other image
from PIL import Image
img = Image.open('sunset-crop.jpg')
pasteImg = Image.open('sunset.jpg')
pasteImg.paste(img, (0,0))
pasteImg.save('pasted.jpg')

#Watermark images
from wand.image import Image

with Image(filename='sunset.jpg') as background:
  with Image(filename='watermark.jpg') as watermark:
    background.watermark(image=watermark, transparency=0.25, left=560, top=300)
    background.save(filename='result.jpg')
