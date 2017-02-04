import sys
from scipy.misc import imread
from scipy.linalg import norm

#Method to compare two images and 
#return the difference in pixels
def compare_images(img1, img2):
    diff = img1 - img2
    z_norm = norm(diff.ravel(), 0)
    return z_norm

#Read two images and get the reader objects
img1 = imread("sunset.jpg").astype(float)
img2 = imread("pasted.jpg").astype(float)

#Actual comparison and retrun difference
z_norm = compare_images(img1, img2)
print "Pixel Difference:", z_norm
