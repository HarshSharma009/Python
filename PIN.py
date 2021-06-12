#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:07:55 2019

@author: root
"""

n=int(input())
l=[int(x) for x in input().split()]
l=list(set(l))
print(l)
setele=int(input())

l1=[]
x,y=0,setele
while len(l[x:y])>=setele:
    l1.append(sum(l[x:y]))
    print(l[x:y])
    y+=setele
    x+=setele
    
if (len(l[x:y])<setele):
    l1.extend(l[x:y])
l1=set(l1)
print(sorted(list(l1)))
