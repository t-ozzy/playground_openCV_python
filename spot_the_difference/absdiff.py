import cv2
from matplotlib import pyplot as plt
# 入力画像1を読み込む
image1 = cv2.imread("saize_left.png")
# 入力画像2を読み込む
image2 = cv2.imread("saize_right.png")
print(image1.shape)
print(image2.shape)
# 画像のサイズが同じであることを確認
if image1.shape != image2.shape:
    print("画像のサイズが異なります。リサイズが必要です。")
    exit
# BGRのチャンネル並びをRGBの並びに変更(matplotlibで結果を表示するため)
rgb_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB) 
rgb_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB) 
# 差分を計算
diff = cv2.absdiff(rgb_image1, rgb_image2)
# グレースケールに変換
diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
# 二値化で異なる部分を強調、背景が白になる様にcv2.THRESH_BINARY_INVを指定
retval, result = cv2.threshold(diff_gray, 50, 255, cv2.THRESH_BINARY)
# 結果の可視化
plt.rcParams["figure.figsize"] = [18,7]                             # ウィンドウサイズを設定
title = "cv2.absdiff: codevace.com"
plt.figure(title)                                                   # ウィンドウタイトルを設定
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)   # 余白を設定

plt.subplot(2,2,1)                                                  # 1行3列の1番目の領域にプロットを設定
plt.imshow(rgb_image1)                                              # 入力画像1を表示
plt.title('image1')                                                 # 画像タイトル設定
# plt.axis("off")                                                     # 軸目盛、軸ラベルを消す
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2)                                                  # 1行3列の2番目の領域にプロットを設定
plt.imshow(rgb_image2)                                              # 入力画像2を表示
plt.title('image2')                                                 # 画像タイトル設定
# plt.axis("off")                                                     # 軸目盛、軸ラベルを消す
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3)                                                  # 1行3列の3番目の領域にプロットを設定
plt.imshow(result, cmap='gray')                                     # 差分の画像を表示
plt.title('subrtacted')                                             # 画像タイトル設定
# plt.axis("off")                                                     # 軸目盛、軸ラベルを消す
plt.xticks([]), plt.yticks([])

plt.show()