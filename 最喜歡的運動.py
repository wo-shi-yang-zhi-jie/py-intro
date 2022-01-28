# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:16:10 2022

@author: yishe
"""

score = []
yn = input('你有喜歡的運動嗎?  y/n:   ')
n = 0 
while yn == 'y':
    w = input('你喜歡甚麼運動?  ' )
    score.append(w)
    x = w
    n = n+1
    if n > 4:
        break
    yn = input('你還有喜歡的運動嗎?  y/n    ')
print(score)
where = input("你喜歡去那裡運動?     ")
score.append(where)
n = input("你想加入甚麼數字??     ")
n = int(n)
score.insert(2,n)
score.remove(x)
print(score)

