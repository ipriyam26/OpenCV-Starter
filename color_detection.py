import cv2
import itertools
import numpy as np
def empty(a):
    return

def stackImages(scale,imgArray):
    rows = len(imgArray)
    rowsAvailable = isinstance(imgArray[0], list)
    if rowsAvailable:
        cols = len(imgArray[0])
        width = imgArray[0][0].shape[1]
        height = imgArray[0][0].shape[0]
        for x, y in itertools.product(range(rows), range(cols)):
            imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale) if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2] else cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)

            if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])
        return np.vstack(hor)
    else:
        for x in range(rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale) if imgArray[x].shape[:2] == imgArray[0].shape[:2] else cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)

            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        return hor



cv2.namedWindow('TrackedBars', cv2.WINDOW_NORMAL)
#change size of window
cv2.resizeWindow('TrackedBars', 640, 240)
cv2.moveWindow('TrackedBars', 1020, 0)
def on_trackbar(val):
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    imgMASK = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=imgMASK)
    imgStack = stackImages(0.6,([img,imgHSV],[imgMASK,imgResult]))
    cv2.imshow("Stacked Images", imgStack)
    # cv2.imshow("Output1", img)
    # cv2.imshow("Output2", imgHSV)
    # cv2.imshow("Mask", imgMASK)
    
cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, on_trackbar)
cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)

img = cv2.imread("cars.jpg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Show some stuff
on_trackbar(0)
# Wait until user press some key
cv2.waitKey()