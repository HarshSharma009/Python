#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 20:31:31 2019

@author: root
"""
c=0
l=[int(x) for x in input().split()]
for i in range(1,4):
    for j in range(l[i],l[0]+1,l[i]):
        if i==1:
            if j%l[2]==0 or j%l[3]==0:
                continue
        elif i==2:
            if j%l[3]==0 or j%l[1]==0:
                continue
        elif i==3:
            if j%l[2]==0 or j%l[1]==0:
                continue
        print(j)
        c+=1
print(c)