import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    laplace = cv2.Laplacian(gray, cv2.CV_64F)
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(laplace,-1,kernel)

    cv2.namedWindow("gray", cv2.WINDOW_NORMAL)
    cv2.imshow('gray',gray)
    cv2.namedWindow("color", cv2.WINDOW_NORMAL)
    cv2.imshow('color',frame)
    cv2.namedWindow("hsv", cv2.WINDOW_NORMAL)
    cv2.imshow("hsv", hsv)
    cv2.namedWindow("laplace", cv2.WINDOW_NORMAL)
    cv2.imshow("laplace", dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
