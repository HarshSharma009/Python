# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:41:35 2021

@author: abcd
"""
def go(ind,n,arr,l):
    global ans
    for i in range(ind+1,n):
        if arr%l[i]==0:
            ans+=max(arr+l[i],ans)
            go(i,n,l[i],l)
    
    return
    
n=int(input())
l=[int(i) for i in input().split()]
ans=0
for i in range(n):
    go(i,n,l[i],l)
ll=[]
for i in range(n):
    for j in range(i+1,n):        
        prev=l[i]
        sum1=l[i]
        for k in range(j,n):
            if l[k]%prev==0:
                prev=l[k]
                sum1+=l[k]
        ll.append(sum1)
print(max(ll))
            