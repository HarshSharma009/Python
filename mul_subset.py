# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:57:24 2020

@author: abcd
"""

for _ in range(int(input())) :
    n,k=map(int,input().split())
    arr = list(map(int,input().strip().split()))
    count,s,pro=0,0,1
    for i in range(n):
        pro*=arr[i]
        #print(pro,count)
        while s<i and pro>=k:
            pro/=arr[s]
            s+=1
        if pro<k:
            length=i-s+1
            count+=length
    print(count)