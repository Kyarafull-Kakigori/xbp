for i in range(3):
    #文字だからダブル区ヲーてションマーク
    print(i,"人目")
    name=input("名前を入れて下さい")

    waist=float(input("腹囲を入れて下さい"))
    age=int(input("年齢を入れて下さい"))
        #ここから先はプリント
    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

        #ここから条件分岐
    if waist>=85 and age>=40:
            print(name,"さん、内臓脂肪蓄積注意です")
    else:
            print(name,"さん、腹囲は問題ありません")
        
    
