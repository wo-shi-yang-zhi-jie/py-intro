# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:00:24 2022

@author: yishe
"""
score = []
g = 0#全班的成績總和
m = 0#最高分
s = 0#最低分
for x in range(5):
    n = input("請輸入成績:    ")
    n = int(n)
    score.append(n)
    g = g + n
    print(score)
    if x >= 1:
        if score[x] >= score[x-1]:
            m = score[x]
        if score[x] <= score[x-1]:
            s = score[x]

print('平均:',g/5)
print("最高分:" ,m)
print("最低分:" ,s)