# ステップ3: 特徴抽出の実践演習
# このファイルの空欄を埋めて、特徴抽出の流れを完成させてください

import cv2
import numpy as np

# 画像を読み込む
image = cv2.imread('free_photo.jpg')

if image is None:
    print("画像が読み込めませんでした")
    exit()

print("元の画像のサイズ:", image.shape)

# =====================================
# ステップ1: 前処理 (Preprocessing)
# =====================================

# 1-1. グレースケール変換
# ヒント: cv2.cvtColor() を使って、BGRからGRAYに変換します
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 1-2. ノイズ除去 (オプション - 今回は省略)

print("グレースケール画像のサイズ:", gray.shape)

# =====================================
# ステップ2: 特徴検出 (Feature Detection) 
# =====================================

# 2-1. エッジ検出 (Canny法)
# ヒント: cv2.Canny() を使って、閾値50と150でエッジを検出します
edges = cv2.Canny(gray, 50, 150)


# 2-2. コーナー検出 (Harris法)
# ヒント: cv2.cornerHarris() を使います
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

print("特徴検出が完了しました")

# =====================================
# ステップ3: 結果の保存と表示
# =====================================

# エッジ検出結果を保存
cv2.imwrite('edges_result.jpg', edges)

# コーナー検出結果を表示するために、元画像にマークを追加
corner_image = image.copy()
corner_image[corners > 0.01 * corners.max()] = [0, 0, 255]  # 赤色でマーク
cv2.imwrite('corners_result.jpg', corner_image)

print("特徴抽出が完了しました！")
print("結果画像:")
print("- edges_result.jpg: エッジ検出結果")
print("- corners_result.jpg: コーナー検出結果")
