# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:10:33 2022

@author: yishe
"""

import random
num = random.randint(1,20)
i = 0 #一輪猜了幾次
o = 5 #還可猜的次數
a = 0 #猜對幾次
b = 0 #總共猜過幾次
while o > 0 :
    ans = input("在1~20中猜個數字吧! 你要猜:    ")
    ans = int(ans)
    if ans == num:
        print("答對了!!")
        i = i+1
        o = 0
        a = a+1
        b = b+1
        print("這一輪中，你猜了",int(i),"次")
        yn = input("你還要玩嗎? y/n:    ")
        if yn == "y":
            o = 5
            i = 0
            num = random.randint(1,20)
        elif yn == "n":
            b = int(b)
            a = int(a)
            print("你總共猜了", b,"次")
            print("你猜中過", a,"次")
            print("平均每", b/a,"次猜中一次")
    elif ans > num:
        print("太大了!!")
        i = i+1
        o = o-1
        b = b+1
        print("你還可再猜",o, "次")
    elif ans < num:
        print("太小了!!")
        i = i+1
        o = o-1
        b = b+1
        print("你還可再猜",o, "次")
if o == 0 :
    print("遊戲結束，下次再來挑戰吧!")    

