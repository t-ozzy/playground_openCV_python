import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('saize_left.png')

# グレースケール変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# しきい値処理（白に近い部分を余白とみなす）
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# 輪郭検出
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 最大の輪郭（＝余白を除いた本体）を取得
x, y, w, h = cv2.boundingRect(contours[0])
for cnt in contours:
    x_, y_, w_, h_ = cv2.boundingRect(cnt)
    if w_ * h_ > w * h:
        x, y, w, h = x_, y_, w_, h_

# トリミング
trimmed = image[y:y+h, x:x+w]

# サイズを統一（例：300x300にリサイズ）
resized = cv2.resize(trimmed, (300, 300))

# 保存
cv2.imwrite('output.png', resized)