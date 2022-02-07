# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:29:53 2022

@author: yishe
"""
scores = ['henry', 83, 'david', 95, 'chris', 92, 'amy', 87, 'bill', 77]

#print(5*2)
#print(len(scores))

# name
names = [scores[i] for i in range(0, len(scores), 2)]
print(names)
    
# score
score = [scores[i+1] for i in range(0, len(scores), 2)]
print(score)

highest = 0
lowest = 100
for x in range(len(names)):
    if score[x] > highest:
        highest = score[x]
    if score[x] < lowest:
        lowest = score[x]
        
print('最高分: ', names[score.index(highest)], highest)
print('最低分: ', names[score.index(lowest)], lowest)
s = 0
for x in range(len(score)):
    s = s + score[x]
print('平均: ', s/5)
    