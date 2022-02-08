# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:02:09 2022

@author: yishe
"""

N = ['Bob','Henry','He','Sam','Judy']
V = ['isn\' t','is','wants to be','like']
n = ['brother','poilce','student','teacher','ironman']
import random
for i in range(5):
    name = random.sample(N,1)
    verb = random.sample(V,1)
    num = random.sample(n,1)
    print(name , verb , num)