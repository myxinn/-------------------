#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author : Myx
# Time   : 2017/7/24 15:05
# File   : test.py


'''
1. 去除所有标点符号；需要去除的标点符号是如下几种: , . ! ? : ;
2. 所有数字包括小数，整数，负数都替换成一个替代字符串: ==NUMBER==
3. 所有大写字母全部转成小写
4. 去除每行起始的所有空格
5. 连续的空格缩短为单独的空格（除每行起始连续空格，见以上规则4）
6 .如果经过上述处理导致一行为空，则在此行处放置标记字符串：[REMOVED] 

'''

with open('test_input-1.txt', 'r') as f:
    tls = []
    while True:
        l = f.readline()
        # l.lower()
        if l == '':
            break

        # l.isdigit()

        # l = test1(l)
        s = []
        for i, t in enumerate(l):
            # 1.去除符号
            if t in [',', '.', '!', '?', ':', ';']:
                t = ''

            # 2. 数字转为特定字符 也可以用ASICII来左，应该美观很多
            if t == '-' and l[i + 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                t = ''
            if t in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if l[i - 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                    t = ''
                else:
                    t = '==NUMBER=='

            # 3. 大写转小写
            if 'A' <= t <= 'Z':
                t = chr(ord(t) + 32)

            # 4. 去除行首空格
            # if l[0] == ' ':
            #     j = 0
            #     while True:
            #         j = j + 1
            #         if l[j] != ' ':
            #             break
            #         t = l[j]
            #         t = ''

            # 5. 连续空格缩短为一个
            if t == ' ' and l[i + 1] == ' ':
                t = ''
            s.append(t)
        l = ''.join(s)

        #  7. 空行替换特定字符
        if l == '' or l == '\n' or l == '\t':
            print(' love worldsss')
            l = '[REMOVED]\n'
        # 4.
        if l[0] == ' ':
            l = l[1:]

        tls.append(l)
    with open('test_output-1.txt', 'w') as f1:
        text = ''.join(tls)
        print((text))
        f1.write(text)







# kk = ",Last month2006,   three of    China's four largest banks reported annual declines in fourth-quarter earnings for the first time since 2009."
# k = "           Tianhe's shares rose rapidly after listing last June but it fell foul of short sellers in September, since when its share price has halved."

# print('l' + test1(t))
# print(kk.strip())
# s = []
# for i, t in enumerate(kk):
#     if t in [',', '.', '!', '?', ':', ';']:
#         t = ''
#     if i < len(kk) - 1:
#         # print(t)
#         if t == ' ' and kk[i + 1] == ' ':
#             t = ''
#         if t in ['0','1','2','3','4','5','6','7','8','9']:
#             if  kk[i - 1] in ['0','1','2','3','4','5','6','7','8','9']:
#                 t = ''
#             else:
#                 # print(kk[i-1])
#                 t = '==NUMBER=='
#
#
#
#
#     s.append(t)
# p = filter(kk.isdigit(), (kk)) /
# print(''.join(s))
# print( filter(kk.isdigit(), 'lo1l23l'))