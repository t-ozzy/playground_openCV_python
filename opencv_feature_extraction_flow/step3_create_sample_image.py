# ステップ3: サンプル画像の作成
# 特徴抽出の練習用に簡単な画像を作成します

import cv2
import numpy as np

# 白い背景の画像を作成（300x300ピクセル）
image = np.ones((300, 300, 3), dtype=np.uint8) * 255

# 画像に簡単な図形を描いて特徴を作る
# 青い四角形を描く
cv2.rectangle(image, (50, 50), (150, 150), (255, 0, 0), 3)

# 緑の円を描く
cv2.circle(image, (200, 100), 50, (0, 255, 0), 3)

# 赤い線を描く
cv2.line(image, (50, 200), (250, 200), (0, 0, 255), 3)

# 画像を保存
cv2.imwrite('sample_image.jpg', image)

print("サンプル画像 'sample_image.jpg' を作成しました！")
print("この画像には四角形、円、線の特徴があります。")
