# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:38:23 2021

@author: abcd
"""

n=int(input())
if n%2:
    print('* '*n)
    st=1
    mid=n*2-1-6
    for i in range(1,n-1):
        if i==n//2:
            print('*'+' '*((n*2-1)//2-1)+'0'+' '*((n*2-1)//2-1)+'*')
        elif i<n//2:
            print('*'+' '*st+'*'+' '*mid+'*'+' '*st+'*')
            st+=2
            mid-=4
        else:
            st-=2
            mid+=4
            print('*'+' '*st+'*'+' '*mid+'*'+' '*st+'*')
    print('* '*n)