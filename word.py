#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:16:09 2019

@author: root
"""

n="""kali is earliest appearance is that of a destroyer of evil forces 
She is the most powerful form of Shakti
and the goddess of one of the four subcategories of the Kulamārga
a category of tantric Saivism"""

l=n.split('\n')

l1=list(x.split() for x in l)
new=[]
for i in range(len(l1)):
    new+=l1[i]
    
d={}
for x in new:
    d[x]=d.setdefault(x,0)+1
print(d)
n1=input("Enter a word: ")
for i in range(len(l)):
    if n1 in l1[i]:
        print("{} present in line {}".format(n1,i+1))
    