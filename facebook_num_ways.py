#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:23:46 2019

@author: root
"""

def helper(data,k):
    if k==0:
        return 1
    s=len(data)-k
    if data[s]=='0':
        return 0
    result=helper(data,k-1)
    if k>=2 and int(data[s:s+2])<=26:
        result+=helper(data,k-2)
    return result

def num_ways(data):
    return helper(data,len(data))


d={}
def helpertd(data,k):
    if d.get(k,-1)!=-1:
        return d[k]
    if k==0:
        return 1
    s=len(data)-k
    if data[s]=='0':
        return 0
    result=helpertd(data,k-1)
    if k>=2 and int(data[s:s+2])<=26:
        result+=helpertd(data,k-2)
    d[k]=result
    return result
    

def num_waystd(data):
    l=len(data)
    return helpertd(data,l)
   

if __name__=='__main__' :
    import timeit
    n=input()
    print(timeit.timeit('print(num_waystd(n))', globals=globals(), number=1))
    print(timeit.timeit('print(num_ways(n))', globals=globals(), number=1))