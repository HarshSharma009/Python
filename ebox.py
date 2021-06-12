#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:48:25 2019

@author: root
"""

f=open('sample.txt')
l=[]
for i in f.read():
    if i.isdigit():
        l.append(int(i))
print("The sum of the integers in the file sample.txt is:{}".format(sum(l)))
"""
#something important
i=int(input());k=1
while~-i%-~k<1:k+=1
print(k)
"""
