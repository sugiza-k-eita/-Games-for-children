#!/usr/bin/env python
# coding: utf-8

#色々な文字で出てくる単語をユーザーに英語で入力してもらい
#覚えてもらおうというゲームです



import time
import random

def pt(message,zikan):
    print(message)
    time.sleep(zikan)
from IPython.display import Image,display

syurui = ["初級コース", 
          "中級コース", 
          "上級コース",
          "中国語コース",
          "韓国語コース",
          "ドイツ語コース"
          ]

naiyou = ["英単語を", 
          "フルーツの名前を英語で", 
          "漢字を英語になおして",
          "中国語を英語になおして",
          "韓国語を英語になおして",
          "ドイツ語を英語になおして"
          ]

momo = "https://2.bp.blogspot.com/-hk6694fQSJw/UgSMTOBJw1I/AAAAAAAAXA0/EEEsX_XD62E/s800/fruit_peach.png"

mikan = "https://4.bp.blogspot.com/-kSVEMERMQNk/UgSMSBgSkhI/AAAAAAAAXAc/IdXkFCEc_4A/s800/fruit_orange2.png"

budou = "https://4.bp.blogspot.com/-CQHQheuBz_o/UgSMPaqr_vI/AAAAAAAAW_Y/HQbcanw26rU/s800/fruit_grape.png"

suika = "https://1.bp.blogspot.com/-wV0uMecKVU4/UYH5pD12L8I/AAAAAAAARI4/rSfLcMXDf-c/s600/suika.png"

melon = "https://2.bp.blogspot.com/-wIs3pMkyXsg/UgSMRuzjm5I/AAAAAAAAXAY/OWFgXcK7cCs/s800/fruit_melon.png"

ichigo = "https://4.bp.blogspot.com/-U_4f-9W0AN0/Vq88_45DLNI/AAAAAAAA3js/IFdRMuEFLM8/s800/fruit_slice05_strawberry.png"

remon = "https://4.bp.blogspot.com/-H83U_NEGoG4/UgSMQ23JTBI/AAAAAAAAXAE/DtbU7N7mugc/s800/fruit_lemon.png"

mango = "https://2.bp.blogspot.com/-QoUNnIJ5oJ0/UgSMQ1mLQhI/AAAAAAAAXAA/eGXVSYHAqnc/s800/fruit_mango.png"

kiui = "https://2.bp.blogspot.com/-Y8xgv2nvwEs/WCdtGij7aTI/AAAAAAAA_fo/PBXfb8zCiQAZ8rRMx-DNclQvOHBbQkQEwCLcB/s800/fruit_kiwi_green.png"

ringo = "https://4.bp.blogspot.com/-uY6ko43-ABE/VD3RiIglszI/AAAAAAAAoEA/kI39usefO44/s800/fruit_ringo.png"

banana = "https://1.bp.blogspot.com/-JaRzIloEZw4/UgSMOL-UzYI/AAAAAAAAW_A/vOiX6Tz5oO4/s800/fruit_banana.png"

pain = "https://2.bp.blogspot.com/-0yLbnxQU0Ws/UgSMTeUiRyI/AAAAAAAAXA4/T3KvqtUp_2w/s800/fruit_pineapple.png"

itijiku = "https://2.bp.blogspot.com/-9NeYTjzxzmQ/UMaeRXUHByI/AAAAAAAAHzA/NLo5oAsgh0I/s1600/fruit_ichijiku.png"

sakurannbo = "https://3.bp.blogspot.com/-ddTjHiYjIjI/UgSMOOCKHeI/AAAAAAAAW-4/QrU2gpketvQ/s800/fruit_cherry.png"





pafe = "https://2.bp.blogspot.com/-4SSFZUa0ab4/Vg57ivCMfhI/AAAAAAAAyzQ/Pm4eBFxAaOc/s800/sweets_fruit_pafe.png"

taruto = "https://1.bp.blogspot.com/-FRSZgid1_h0/VkxN0jCi5XI/AAAAAAAA00E/xPxeaVzd9fI/s800/sweets_fruit_tarte.png"

mitumame = "https://2.bp.blogspot.com/-4k0WpkLJjbk/W8BOiyhS36I/AAAAAAABPaY/_YzqaUA7z9AHQQ1blLr5T5tNH4K_Zb4TgCLcBGAs/s800/sweets_fruit_mitsumame.png"

sando = "https://www.irasutoya.com/2016/06/blog-post_66.html"

moriawase = "https://2.bp.blogspot.com/-HkUFBkdr47g/VNH7SHKrR3I/AAAAAAAArcc/I6wtni7OXEY/s800/cut_fruit_moriawase.png"


fruit_img = [momo, 
             mikan, 
             budou, 
             suika, 
             melon, 
             ichigo, 
             remon, 
             mango, 
             kiui, 
             ringo, 
             banana, 
             pain, 
             itijiku,
             sakurannbo
             ]

fruit_eng = ["peach",
             "orange",
             "grape",
             "watermelon",
             "melon",
             "strawberry",
             "lemon",
             "mango",
             "kiwi",
             "apple",
             "banana",
             "pineapple",
             "fig",
             "cherries"
             ]

fruit_kana = ["モモ",
              "オレンジ",
              "グレープ",
              "スイカ",
              "メロン",
              "ストロベリー",
              "レモン",
              "マンゴー",
              "キウイ",
              "リンゴ",
              "バナナ",
              "パイナップル",
              "イチジク",
              "サクランボ"
              ]

fruit_kanji = ["桃",
               "蜜柑",
               "葡萄",
               "西瓜",
               "甜瓜",
               "苺",
               "檸檬",
               "芒果（檬果）",
               "彌猴桃",
               "林檎",
               "甘蕉（芭蕉実）",
               "鳳梨酥",
               "無花果",
               "桜桃"
               ]


fruit_china = ["桃子",
               "桔子",
               "葡萄",
               "西瓜",
               "哈密瓜",
               "草莓",
               "柠檬",
               "芒果",
               "猕猴桃",
               "苹果",
               "香蕉",
               "菠萝",
               "无花果",
               "樱桃"
               ]


fruit_korean = ["복숭아",
                "귤",
                "포도",
                "수박",
                "멜론",
                "딸기",
                "레몬",
                "망고",
                "키위",
                "사과",
                "바나나",
                "파인애플",
                "무화과",
                "앵두"
                ]

fruit_doitu = ["Pfirsich",
               "Mandarine",
               "Trauben",
               "Wassermelone",
               "Melone",
               "Erdbeere",
               "Zitrone",
               "Mango",
               "Kiwi",
               "Apfel",
               "Banane",
               "Ananas",
               "Feige",
               "Kirsche"
               ]



gohoubi = [pafe, taruto, mitumame, sando, moriawase]

fruit_kara = []

fruit_kara2 = []

pt("英単語プログラムはじまるよ！", 2)
user = input("あなたの名前を教えてね")

pt(user + "！よろしくね！", 2)
pt("勉強やバイトで疲れている" + user + "にデザートをプレゼントしたいな～", 2)
pt("正答数に応じて用意してあるから頑張ってね～♪", 2)

while True:
    nanido = int(input('''やりたい難易度を選択してね
                       1:初心者コース
                       2:中級コース
                       3:上級コース
                       '''))
#ここでコースの分岐をしています↓
    if nanido == 1:
        i = 0
        fruit_kara.extend(fruit_eng)
        break
    elif nanido == 2:
        i = 1
        fruit_kara.extend(fruit_kana)
        break
    elif nanido ==3:
        i = 2
        fruit_kara.extend(fruit_kanji)
        break
    else:
        pt("こらこら！１～３から選んでね…！", 2)


#用意しておいた空のlistに分岐した際にそれぞれの内容を入れることで
#初級コース、中級コース、上級コースを一つにまとめました↓
point1 = 0
pt(syurui[i] + "だよ！", 1)
pt("表示される" + naiyou[i] + "入力してね！", 2)
pt("正確に入力できれば1問につき1つの果物をゲットできるよ！", 2)
pt("全部で10問！全問正解目指して頑張ろう！", 2)
for u in range(1,11):
    pt("", 1)
    print("第", u, "問")
    index = random.randint(0, len(fruit_kara) - 1)
    pt(fruit_kara[index], 1)
    answer1 = str(input("あなたの答えをどうぞ"))
    
    if answer1 == fruit_eng[index]:
        pt("正解！1個ゲットだよ～！", 1)
        point1 = point1 + 1
        pt("", 1)
        print("現在の果物：", point1, "個")
    else:
        pt("残念でした", 2)
        display(Image(fruit_img[index]))
        pt("正解は" + fruit_eng[index] + "です！", 2)
        point1 = point1
        print("現在の果物：", point1, "個")
 


#正解数ごとにスイーツの内容を分岐しました ↓     
if point1 == 10:
    pt("", 2)
    pt("全問正解した" + user + "にご褒美だよ！", 1)
    display(Image(gohoubi[4]))
    pt("フルーツの盛り合わせを", 1)
        
elif point1 <= 9 or point1 >= 5 :
    pt("", 2)
    print("果物をたくさん手に入れた", user, "に")
    pt("おいしいスイーツのご褒美だよ！！", 1)
    
    while True:        
        tokuchou = int(input('''生クリームは好きかな？
                     1：好き
                     2：嫌い
                     '''))
        
        if tokuchou == 1:
           pt("生クリームが大好きな" + user + "にはこれ！！", 1)
           display(Image(gohoubi[0]))
           pt("パフェを", 1)
           break
      
        elif tokuchou == 2:
           pt("生クリームが嫌いな" + user + "にはこれ！！", 1)
           display(Image(gohoubi[2]))
           pt("フルーツ豆みつを", 1)
           break
        else:
           pt("ちゃんと１か２で選んでね……", 2)
      
        
else:
    pt("", 2)
    pt("がんばった" + user + "にはご褒美だよ～")
    display(Image(gohoubi[3]))

time.sleep(2)    
pt("どうぞ召し上がれ♪♪", 2)

#チャレンジ問題としてさらに5問追加しました↓
while True:
    
    print("ここで" + user + "にはチャレンジ問題に挑戦してほしいな～！")
    time.sleep(2)
    print('''
          １：中国語
          ２：韓国語
          ３：ドイツ語
             ''')
    time.sleep(1)
    charenge = int(input('''
                         おすすめは中国語だよ！
                         知識がなくても読める可能性があるからね♪
                         どれにする？'''))
#先ほどと同様にコースの分岐をここでします↓
        
    if charenge == 1:
        i = 3
        fruit_kara2.extend(fruit_china)
        break
    elif charenge == 2:
        i = 4
        fruit_kara2.extend(fruit_korean)
        break
    elif charenge == 3:
        i = 5
        fruit_kara2.extend(fruit_doitu)
        break
            
    else:
        pt("こらこら！１～４から選んでね…！")
 

#中国語コース、韓国語コース、ドイツ語コースを一つにまとめました↓
        
point2 = 0       
pt(syurui[i] + "だよ！", 1)
print("表示される" + naiyou[i] + "入力してね！")
for u in range(11,16):
    pt("", 1)
    print("第", u, "問")
    index = random.randint(0, len(fruit_kara2) - 1)
    pt(fruit_kara2[index], 1)
    answer2 = str(input("あなたの答えをどうぞ"))
    
    if answer2 == fruit_eng[index]:
        pt("正解！すごい！物知りだね！", 1)
        point2 = point2 + 1
        pt("", 1)
    else:
        pt("残念でした～", 2)
        display(Image(fruit_img[index]))
        pt("正解は" + fruit_eng[index] + "です！", 2)
        pt("諦めないで～", 1)
        point2 = point2


 
pt("お疲れ様でした～", 1)

#綴りを確認できるようにしました↓

pt("色々なフルーツの名前を確認できるよ～", 1)
pt("時間があればどんな風に表現されるのか見ていってね！", 1)
while True:
    ans1 = int(input('''
                 フルーツの名前の確認をしていく？？
                 １：する
                 ２：しない
                 '''))
    if ans1 == 1:
        pt("お！！じゃあ、いくよー！", 2)
        pt("進みたいときはエンターキーを押してね～", 1)
        for g in range(0,14):
            display(Image(fruit_img[g]))
            print("中国語では" + fruit_china[g] + "で")
            print("韓国語では" + fruit_korean[g] + "で")
            print("ドイツ語では" + fruit_doitu[g] + "だよ～")
            input()
            
        break
    elif ans1 == 2:
        pt("そっか！また今度だね", 1)
        break
        
    else:
        pt("こらこら！１か２から選んでね…！", 1)


#最後に合計で何問正解したのか質問します 
pointsum = point1 + point2      
pt("最後に質問するよ", 1)
ans = int(input(user + "が正解した数はいくつか覚えてる？？"))
if ans == pointsum:
    pt("すごい…！よく覚えていたね",2)
else:
    pt("残念…！！", 1)
    print("正解は")
    print(pointsum)
    print("だよ～")
    


pt("これで終了だよ！", 2)

pt("楽しんでもらえたかな？また遊びにきてね～♪♪", 1)



