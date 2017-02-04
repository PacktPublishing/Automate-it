#Program for face detection
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade.xml')
original_image_path = 'Chetan.jpeg'

image = cv2.imread(original_image_path)
faces = face_cascade.detectMultiScale(
    image, scaleFactor=1.1, minNeighbors=3,
    minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('chetan_face.jpg', image)
