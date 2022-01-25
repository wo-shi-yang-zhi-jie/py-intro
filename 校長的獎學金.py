# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:00:09 2022

@author: yishe
"""

math = input("輸入數學成績:    ")
eng = input("輸入英文成績:    ")
math = int(math)
eng = int(eng)

if math >= 90 and eng >=90:
    print("考得很好有獎學金!")
elif math == 100 or eng == 100:
    print("考得很好有獎學金!")
else:
    print("再接再厲!")