#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:14:05 2019

@author: root
"""
#Nptel solution
"""
def solve(l1,l2):
    n = len(l1)
    
    if n == 0:
        return(0)

    ans = [0 for i in range(n+1)]
    
    ans[n-1] = max(l1[n-1],l2[n-1]) - min(l1[n-1],l2[n-1])

    for i in range(n-2,-1,-1):
        vert = max(l1[i],l2[i]) - min(l1[i],l2[i]) + ans[i+1]
        horz = max(l1[i],l1[i+1]) - min(l1[i],l1[i+1]) + max(l2[i],l2[i+1]) - min(l2[i],l2[i+1]) + ans[i+2]
        ans[i] = max(vert,horz)

    return(ans[0])

nstr = input()
# Value of n not needed in Python
#  n = int(nstr.strip())

# Read and parse first row of numbers
line1str = input().strip()
line1strlist = line1str.split()
line1 = []
for s in line1strlist:
    line1.append(int(s))

# Read and parse second row of numbers
line2str = input().strip()
line2strlist = line2str.split()
line2 = []
for s in line2strlist:
    line2.append(int(s))

print(solve(line1,line2))
"""
n=int(input())
a=list(map(int,input().split()))
a_1=list(map(int,input().split()))
ps=0
f=abs(a[0]-a_1[0])
for i in range(1,n):
  vp=f+abs(a[i]-a_1[i])
  hp=ps+abs(a[i]-a[i-1])+abs(a_1[i]-a_1[i-1])
  ps=f
  f=max(vp,hp)
print(f)