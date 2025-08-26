import cv2
import numpy as np

def nothing(x): #これ何？ ダミーコールバック
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8) #300,512,3って何の値？ h,w,色チャンネル数
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #esc
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image') #なんで'image','R'じゃないの？ 決まり
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')

    img[:] = [b,g,r]

cv2.destroyAllWindows()
