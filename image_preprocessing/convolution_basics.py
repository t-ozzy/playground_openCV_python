import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('sample.jpg')


# 3x3の平均化フィルタ
kernel = np.ones((3, 3), np.float32) / 9
# 畳み込みの適用
smoothed_image = cv2.filter2D(image, -1, kernel)
# 結果の表示
# cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 水平方向のSobelフィルタ
sobel_horizontal = np.array([[-1, 0, 1],
                             [-2, 0, 2],
                             [-1, 0, 1]])
# 畳み込みの適用
edges_horizontal = cv2.filter2D(image, -1, sobel_horizontal)
# 結果の表示
# cv2.imshow('Original Image', image)
cv2.imshow('Horizontal Edges', edges_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()