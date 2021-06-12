# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:05:38 2020

@author: abcd
"""

def trip(w,n):
    w.sort()
    left_index=0
    trips=0
    for i in range(n-1,-1,-1):
        if w[i]>1.99:
            trips+=1
        elif w[i]<=1.99:
            if w[i]+w[left_index]<=3:
                left_index+=1
            trips+=1
        if left_index>=i:
            break
    return trips
n=int(input())
l=list(map(float,input().split()))
print(trip(l,n))
    