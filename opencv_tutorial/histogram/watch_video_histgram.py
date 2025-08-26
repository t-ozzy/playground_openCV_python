import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

while(1):

    # Take each frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    hist = cv2.calcHist([frame], [2], None, [256], [0, 256])
    hist_img = np.zeros((200, 256, 3), dtype=np.uint8)
    cv2.normalize(hist, hist, 0, 200, cv2.NORM_MINMAX)
    for x, y in enumerate(hist):
        cv2.line(hist_img, (x, 200), (x, 200 - int(y[0])), (0, 0, 255), 1)

    cv2.imshow('frame', frame)
    cv2.imshow('histogram', hist_img)

    if cv2.waitKey(5) & 0xFF == 27: #esc
        break

cap.release()
cv2.destroyAllWindows()