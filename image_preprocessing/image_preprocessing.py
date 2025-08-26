import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('sample.jpg')


# リサイズ（200x200ピクセル）
resized_image = cv2.resize(image, (200, 200))
# リサイズした画像を表示
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 正規化（0〜1の範囲）
normalized_image = image / 255.0
# 正規化後の画像データを確認
print(normalized_image)


# ガウシアンブラーを適用（カーネルサイズ：15x15）
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
# ぼかした画像を表示
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# エッジ検出
edges = cv2.Canny(image, 100, 200)
# エッジを検出した画像を表示
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # 平均化フィルタを適用（カーネルサイズ：5x5）ガウシアンブラーのほうがエッジが残りやすい
# smoothed_image = cv2.blur(image, (5, 5))
# # 平滑化した画像を表示
# cv2.imshow('Smoothed Image', smoothed_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 回転行列を作成（中心を基準に45度回転）
height, width = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
# アフィン変換を適用して画像を回転
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
# 回転した画像を表示
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 画像の左右反転
flipped_image = cv2.flip(image, 1)
# 反転した画像を表示
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

