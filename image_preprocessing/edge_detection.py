import cv2
import numpy as np

# 画像の読み込み（グレースケール）
image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)


# Sobelフィルタを適用（X方向）
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
# Sobelフィルタを適用（Y方向）
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
# エッジの強度を計算
sobel_edge = cv2.magnitude(sobel_x, sobel_y)
# 結果の表示
# cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge', sobel_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Canny法によるエッジ検出
# edges = cv2.Canny(image, 100, 200)
# # 結果の表示
# cv2.imshow('Original Image', image)
# cv2.imshow('Canny Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()