import cv2
import matplotlib.pyplot as plt

# 画像の読み込み
image = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

# ORB特徴量検出器の生成
orb = cv2.ORB_create()

# 特徴点の検出
keypoints, descriptors = orb.detectAndCompute(image, None)

# 特徴点を画像に描画
output_image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 結果を表示
plt.imshow(output_image, cmap='gray')
plt.title("ORB Keypoints")
plt.show()