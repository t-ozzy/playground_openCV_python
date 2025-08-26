import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    hist = cv2.calcHist([frame], [2],  None, [256], [0, 256])

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_skin = np.array([0, 20, 70])  # 肌色の下限値 (H, S, V)
    upper_skin = np.array([20, 255, 255])  # 肌色の上限値 (H, S, V)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27: #esc
        break

cv2.destroyAllWindows()