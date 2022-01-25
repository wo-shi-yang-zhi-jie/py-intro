# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:51:39 2022

@author: yishe
"""

grade = input("輸入成績:    ")

grade = int(grade)

if grade >= 90:
    print("A")
elif grade >= 75:
    print("B")
elif grade >= 60:
    print("C")
else:
    print("D")
