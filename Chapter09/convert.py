#Convert colored image to black and white
from PIL import Image
img = Image.open('beach_sunset.png').convert('L')
img.show()
img.save('beach-sunset-gray.png','png')

#Convert png image to jpg format
from PIL import Image
img = Image.open('beach_sunset.png')
img.save('beach-sunset-conv.jpg','jpeg')
