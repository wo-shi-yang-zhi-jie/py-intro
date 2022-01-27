# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:27:50 2022

@author: yishe
"""
#法一
for num in range(1,51):
    num = int(num)
    if num % 3 == 0:
        print(num)
#法二
for i in range(3, 50, 3):
    print(i)
