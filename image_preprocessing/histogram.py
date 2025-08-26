import cv2
import matplotlib.pyplot as plt

# 画像の読み込み（グレースケール）
image = cv2.imread('histogram.jpg', cv2.IMREAD_GRAYSCALE)

# ヒストグラムの計算
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
print(hist)

# ヒストグラムの表示
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()