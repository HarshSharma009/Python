#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:31:09 2019

@author: root
"""

p=[1,5,8,9,10,17,17,20,24,30]


def mc(p,n):
    if n==0:
        return 0
    else:
        r=0
        for i in range(1,len(p)+1):
            if i<=n:
                r=max(r,p[i-1]+mc(p,n-i))
    return r
d={}
cost={0:0}
def td(p,n):
    
    if d.get(n,-1)!=-1:
        return d[n]
    
    else:
        if n==0:
            r=0
        else:
            r=0
            for i in range(1,len(p)+1):
                if i<=n:
                    r=max(r,p[i-1]+td(p,n-i))
    d[n]=r

    return r

def bu(p,n):
    for j in range(1,n+1):
        s=-99999999
        for i in range(1,len(p)+1):
                if j>=i:
                    s=max(s,p[i-1]+cost[j-i])
        cost[j]=s

    return cost[n]

if __name__=='__main__':
    n=int(input())
    import timeit
    print(timeit.timeit('print(td(p,n))', globals=globals(), number=1))
    """
    start=timeit.default_timer()
    print(bu(p,n))
    end=timeit.default_timer()
    print(end-start)
    """