import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640) # set Width
cap.set(4, 480) # set Height
while True:
    success,img = cap.read()
    flip = cv2.flip(img, 1)
    cv2.imshow("Live Video",flip)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break