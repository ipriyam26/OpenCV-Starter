import cv2
import itertools
import numpy as np

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



img = cv2.imread('cars.jpg')
# img2 = cv2.imread('human.jpg')
# img2_resize = cv2.resize(img2, (img.shape[1], img.shape[0]))

imgStack = stackImages(0.5, ([img, img, img], [img, img, img]))

cv2.imshow('Stacked Images', imgStack)

cv2.waitKey(0) 