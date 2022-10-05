from multiprocessing.connection import wait
import cv2

img = cv2.imread("cars.jpg")
shape = img.shape
aspect_ratio = shape[1]/shape[0]
small_size = (int(480*aspect_ratio), 480)

#resize the image
imgResize = cv2.resize(img,small_size)

#cropped image
imgCropped = img[0:4080, 0:2080]

# cv2.imshow("Image",img)
# cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)