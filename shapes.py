from turtle import width
import cv2
import numpy as np

img = cv2.imread("cars.jpg")

shape = img.shape
aspect_ratio = shape[1]/shape[0]
width,height = 480, int(aspect_ratio*480)

pts1 = np.float32([[2440,1170],[770,2800],[3640,2680],[1860,4650]])

pts2 = np.float32([[0,0],[0,width],[0,height],[width,height]])


matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",imgOutput)
cv2.waitKey(0)