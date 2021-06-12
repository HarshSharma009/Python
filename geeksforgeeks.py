# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:57:48 2020

@author: abcd
"""
'''
#LRU
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    c=int(input())
    ans=0
    l=[]*(c+5)
    for i in range(n):
        if len(l)<c and arr[i] not in l:
            l.append(arr[i])
            ans+=1
        elif arr[i] not in l and len(l)>=1 :
            del l[0]
            l.append(arr[i])
            ans+=1
        elif arr[i] in l:
            ind=l.index(arr[i])
            j=arr[i]
            del l[ind]
            l.append(j)
            # print(l)

    print(ans)
'''
for _ in range(int(input())):
    n,k=map(int,input().split())
    if k>n*9 or (n>1 and k=0):
        print('-1')
    else:
        tmp=0
        while k>0:
            if k>9:
                tmp=tmp*10+9
                k=k-9
            else:
                tmp=tmp*10+k
                break
        print(str(tmp).ljust(n,'0'))