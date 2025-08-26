import cv2

# 画像の読み込み（グレースケール）
image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)


# 固定しきい値による二値化
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# 結果の表示
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 大津の二値化
_, otsu_binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 結果の表示
cv2.imshow('Original Image', image)
cv2.imshow('Otsu Binary Image', otsu_binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 適応的二値化（平均値法）
adaptive_binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# 適応的二値化（ガウシアン法）
adaptive_gaussian_binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# 結果の表示
cv2.imshow('Original Image', image)
cv2.imshow('Adaptive Mean Binary Image', adaptive_binary_image)
cv2.imshow('Adaptive Gaussian Binary Image', adaptive_gaussian_binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()