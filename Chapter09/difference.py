from PIL import Image, ImageChops

#Returns the difference between two images as an image
def differnce_images(path_one, path_two, diff_save_location):
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    #Difference calculated here
    diff = ImageChops.difference(image_one, image_two)

    #Method to check if there is no difference
    if diff.getbbox() is None:
        print "No difference in the images"
        return
    else:
        print diff.getbbox()
        diff.save(diff_save_location)

differnce_images('sunset.jpg','pasted.jpg',
                   'diff.jpg')
