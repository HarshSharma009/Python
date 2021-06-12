#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:51:25 2019

@author: root
"""

"""
n1=eval(input())

tar=int(input())

l=[]
for i in n1:
    l+=[tar-i]
for i in range(len(l)):
    if l[i] in n1:
        print(i,n1.index(l[i]))
        break
"""
import re
n=[x for x in input().split()]
for i in n:
    if i[0]!='@' and '@' in i:
        print(i)
        a=re.match(r'(\w+)@(\w+)\.(\w+)',i)
        print(a.group(1))
        print(a.group(2))
        print(a.group(3))
        break
    
    
p=int(input())
g=int(input())
r=int(input())
o=int(input())
cost=int(input())
tmp=cost
count=0
min=1000000
for j in range((cost//p)+1):
    for k in range((cost//g)+1):
        for l in range((cost//r)+1):
            for m in range((cost//o)+1):
                if j*p+k*g+l*r+m*o==cost:
                    count+=1
                    if(j+k+l+m<min):
                        if(j+k+l+m)!=0:
                            min=j+k+l+m
                    print('# of PINK is {} # of GREEN is {} # of RED is {} # of ORANGE is {}'.format(j,k,l,m))
print("Total combinations is {}".format(count))
print("Minimum number of tickets to print is {}".format(min))