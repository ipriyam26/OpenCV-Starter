
import cv2
import numpy as np
#read the image
img = cv2.imread("human.jpg")
# cv2.imshow("Human",img)

#convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Human",imgGray)

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# cv2.imshow("Blur Human",imgBlur)

imgCanny = cv2.Canny(img, 50, 80)
cv2.imshow("Canny Human",imgCanny)

#kernel
kernel = np.ones((5,5), np.uint8)

#image dilation
imgDilation = cv2.dilate(imgCanny, kernel=kernel, iterations=1)
cv2.imshow("Dilation Human",imgDilation)


#wait for a key press
cv2.waitKey(0)