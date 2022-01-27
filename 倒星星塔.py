# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:37:57 2022

@author: yishe
"""

#法一:for
floor = input("你想要幾層的倒星星塔?   "  )#這邊輸入十層就會有十層
floor = int(floor)
for num in range(floor,1-1,-1):
    print('*'*num)

#法二:while
floor = input("你想要幾層的倒星星塔?   "  )
floor = int(floor)
while  floor >= 1:
    print('*'*floor)
    floor = floor - 1
