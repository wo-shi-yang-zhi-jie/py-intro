# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:25:37 2022

@author: yishe
"""

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d.pop('c')
print(len(d))
print('c' in d)
d2 = {'c' :33}
d.update(d2)
print(d)
print(d2)
for i,v in d.items():
    print(i,v)

