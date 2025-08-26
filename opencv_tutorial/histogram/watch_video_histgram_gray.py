import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    
    hist_img = np.zeros((200, 256, 3), dtype=np.uint8)
    cv2.normalize(hist, hist, 0, 200, cv2.NORM_MINMAX)
    for x, y in enumerate(hist.ravel()):
        cv2.line(hist_img, (x, 200), (x, 200 - int(y)), (0, 0, 255), 1)

    cv2.imshow('frame', frame)
    cv2.imshow('histogram', hist_img)

    #esc
    if cv2.waitKey(5) & 0xFF == 27: break

cv2.destroyAllWindows()