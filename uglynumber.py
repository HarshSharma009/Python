# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:03:49 2020

@author: abcd
"""

num = [1]
p2,p3,p5 = 0,0,0

while len(num)<12340:
    next1 = min(2*num[p2], 3*num[p3], 5*num[p5])
    num.append(next1)
    if next1 == 2*num[c2]:
        p2 += 1
    if next1 == 3*num[c3]:
        p3 += 1
    if next1 == 5*num[c5]:
        p5 += 1
for _ in range(int(input())):
    n=int(input())
    print(num[n-1])