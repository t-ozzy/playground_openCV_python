import cv2
import matplotlib.pyplot as plt

# 画像の読み込み
image = cv2.imread("input_image.jpg", cv2.IMREAD_GRAYSCALE)

# SURF特徴量検出器の生成（注意：OpenCVの一部バージョンでのみ利用可能）
surf = cv2.xfeatures2d.SURF_create()

# 特徴点の検出
keypoints, descriptors = surf.detectAndCompute(image, None)

# 特徴点を画像に描画
output_image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 結果を表示
plt.imshow(output_image, cmap='gray')
plt.title("SURF Keypoints")
plt.show()