# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:07:54 2020

@author: Harsh sharma
"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    mid=int((n-1)/2)
    flag=True
    k=n%2+1
    for j in range(mid+1,n):
        if l[j]<l[j-k]:
            flag=False
            break
        elif l[j]>l[j-k]:
            break
        k+=2
    if flag:
        while mid>=0:
            if l[mid]==9:
                l[mid]=0
                mid-=1
            else:
                l[mid]+=1
                break
        else:
            l=[1]+l
            n+=1
    mid=int((n-1)/2)
    if n>1:
        l=l[:mid+1]+l[mid-(n%2)::-1]
    print(*l,sep=" ")