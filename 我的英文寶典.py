# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:07:02 2022

@author: yishe
"""

# title
print('# '*10)
print('我的英文寶典')
print('# '*10)
d = {}#英文字典
d2 = {}#中文字典
d0 = []
import random
# 系統(迴圈)
while True:
    # 功能
    print('\n')
    print('功能=>')
    print('1.建立字彙')
    print('2.列出全部單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開系統')

    sel = input('請輸入欲執行之選項: ')

    # 選項判斷
    if sel == '1':  # 建立字彙
        a = input('輸入你要建立的單字: ')
        b = input('輸入此單字的意思: ')
        print('\n')
        d[a] = b
        d2[b] = a
        d0.append(a)
        print(a,d[a])
        print('\n')
        print('建立成功!')
    elif sel == '2':  # 列出單字
        print(d)
    elif sel == '3':  # 英翻中
        a = input('輸入你要翻譯的單字:  ')
        print('\n')
        if a in d:
            print(d[a])
        else:
            print('單字: {} 不存在本字典'.format(a))
            new = input('是否要建立新字彙? Y/N: ')
            if new == 'Y':
                b = input('請輸入此字彙的意思:   ')
                print('\n')
                d[a] = b
                d2[b] = a
                d0.append(a)
                print(a,d[a])
                print('\n')
                print('建立成功!')
            else:
                pass
    elif sel == '4':  # 中翻英
        b = input('輸入你要翻譯的中文:  ')
        print('\n')
        if b in d2:
            print(d2[b])
        else:
            print('字彙: {} 不存在本字典'.format(b))
            new = input('是否要建立新字彙? Y/N:  ')
            if new == 'Y':
                a = input('請輸入此字彙英文:   ')
                print('\n')
                d2[b] = a
                d[a] = b
                d0.append(a)
                print(b,d2[b])
                print('\n')
                print('建立成功!')
            else:
                pass
    elif sel == '5':  # 測驗學習成果
        x = 0
        y = 0
        for i in range(10):
            q = random.sample(d0,1)[0]
            print(q)
            ans = input('意思是甚麼?  ')
            if ans == d[q]:
                print('你答對了!')
                x = x+1
                print('\n')
            else:
                print('錯了~')
                print('答案是: ', d[q])
                print('\n')
        print('你答對了', x, '題!  ', '得到', x*10, '分!')
    elif sel == '6':  # 離開系統
        break
    else:
        print('wrong input')
