# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:40:57 2022

@author: yishe
"""
scores = [['henry', 97],
         ['david', 98],
         ['bill', 87],
         ['amy', 90],
         ['chirs', 96]]

name = [scores[i][0] for i in range(len(scores))]
print(name)

score = [scores[i][1] for i in range(len(scores))]
print(score)

Max = score.index(max(score))
print('最高分: ', name[Max], score[Max] )

Min = score.index(min(score))
print('最低分: ', name[Min], score[Min])

s = 0
for x in range(len(score)):
    s = s + score[x]
print('平均: ', s/5)


