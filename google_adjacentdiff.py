# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:30:45 2020

@author: abcd
"""

def check(n):
    le=len(n)
    for i in range(le-1):
        if abs(n[i]-n[i+1])!=1:
            return False
    return True

n=int(input())
for i in range(n+1):
    if n<11:
        print(i,end=' ')
    elif check([int(j) for j in str(i)]):
        print(i,end=' ')