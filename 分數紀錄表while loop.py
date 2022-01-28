# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 10:09:47 2022

@author: yishe
"""

score = []
print(score)
i = 0#已輸入的次數
g = 0#全班的成績總和
m = 0#最高分
s = 0#最低分
while i < 5:#全班五人
    n = input("請輸入成績:    ")
    n = int(n)
    score.append(n)
    i = i+1
    if i == 1:
        m = score[i-1]
        s = score[i-1]
    g = g + n
    if i >= 2:
        if score[i-1] > score[i-2]:
            m = score[i-1]
        if score[i-1] < score[i-2]:
            s = score[i-1]
    print(score)
print('平均:',g/5)
print("最高分:" ,m)
print("最低分:" ,s)

