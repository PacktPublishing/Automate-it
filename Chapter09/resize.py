#Resize images in pixels
from PIL import Image
img = Image.open('sunset.jpg')
resized = img.resize((256,256))
resized.save('sunset-resize.jpg', 'jpeg')

#Create thumbnail for a given image
import os, sys
from PIL import Image
size = 128, 128
infile = "sunset.jpg"
outfile = os.path.splitext(infile)[0] + ".thumbnail.jpg"
if infile != outfile:
    try:
        im = Image.open(infile)
        im.thumbnail(size, Image.BICUBIC)
        im.save(outfile, "JPEG")
    except IOError:
        print "cannot create thumbnail for '%s'" % infile

#Crop an image based on pixels from top, left, bottom and right
from PIL import Image
img = Image.open('sunset.jpg')
cropImg = img.crop((965, 700, 1265, 960))
cropImg.save('sunset-crop.jpg')
