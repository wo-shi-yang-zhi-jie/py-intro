# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:51:05 2022

@author: yishe
"""

#讓學生輸入成績，
math = input("輸入數學成績:    ")
eng = input("輸入英文成績:    ")
math = int(math)
eng = int(eng)

if math >= 90 and eng >=90:
    print("考得很好有獎品!")
elif math < 60 and eng < 60:
    print("不及格要處罰!")
else:
    print("再接再厲!")
    