# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:49:59 2022

@author: yishe
"""

#法一:for
floor = input("你想要幾層的星星塔?    "     )
floor = int(floor)
for num in range(1,floor+1):
    print('*'*num)

#法二:while
floor = input("你想要幾層的星星塔?    "     )
floor = int(floor)
i = 1
while i <= floor:
    print('*'*i)
    i = i + 1
