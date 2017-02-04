from PIL import Image

#Get the image object
img = Image.open('sunset.jpg')

#Rotate the image by 180 deg
img.rotate(180).save('sunset180deg.jpg')

#Flip the images horizontally and vertically
img.transpose(Image.FLIP_LEFT_RIGHT).save('sunset_horizontal_flip.png')
img.transpose(Image.FLIP_TOP_BOTTOM).save('sunset_vertical_flip.png')
