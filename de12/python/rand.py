import random
import time

# ことわざリスト
kotowaza_list = ["さるもきからおちる", "じゃのみちはへび", "にとうおうものはいっとうもえず", "でるくいはうたれる", "はなよりだんご", "うりのつるにはなすびにならず", "いのなかのかわずたいかいにでず"]

# ゲームのメインループ
score = 0

input("エンターキーを押してスタート！")

start_time = time.time()

for kotowaza in kotowaza_list:
    print(f"ひらがな: {kotowaza}")
    
    input_text = input("ひらがなで入力してください: ")
    
    if input_text == kotowaza:
        print("正解です！")
        score += 1
    else:
        print("不正解です。")

end_time = time.time()

elapsed_time = end_time - start_time

if elapsed_time < 100:
    print(f"ゲーム終了！正答率: {score}/7, 得点: {score}/10")
else:
    print("タイムアップ")

# 得点に応じ再挑戦のオプションを提供
retry = input("もう一度プレイしますか？ (はい/いいえ): ")
if retry.lower() == "はい":
    # ゲームをリセットして再挑戦
    score = 0