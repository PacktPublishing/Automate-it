#Scan an image and read the contents of scanned image

from pyimagesearch.transform import four_point_transform
from pyimagesearch import imutils
from skimage.filters import threshold_adaptive
import cv2

#Open the image for reading
image = cv2.imread("murray.jpg")
ratio = image.shape[0] / 500.0
orig = image.copy()

#Resize image for reading and apply filters
image = imutils.resize(image, height = 500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
cv2.imwrite('scan_edge.jpg', edged)

#Find image contours and highlight them
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	if len(approx) == 4:
		screenCnt = approx
		break
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imwrite('scan_contours.jpg', image)

#Apply tranformation and get the final scanned image
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
warped = threshold_adaptive(warped, 251, offset = 10)
warped = warped.astype("uint8") * 255
cv2.imwrite('scanned.jpg', warped)

#Read the contents of scanned image
print "Printing the contents of the image:"
from PIL import Image
img = Image.open("scanned.jpg")
import pytesseract
print(pytesseract.image_to_string(img))
