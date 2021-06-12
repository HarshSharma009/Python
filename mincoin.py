#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
def mincoin(n):
    if n==0:
        return 0
    elif n>=5:
        return n//5+mincoin(n%5)
    elif n>=2:
        return n//2+mincoin(n%2)
    else:
        return n//1+mincoin(n%1)
    
print(mincoin(17))
"""
import sys
def mincoin(n,l):
    if n==0:
        return 0
    else:
        r=sys.maxsize
        for i in l:
            if i<=n:
                r=min(r,1+mincoin(n-i,l))
    return r
d={0:0}
def td(n,l):
    
    if d.get(n,-1)!=-1:
        return d[n]
    
    else:
        if n==0:
            r=0
        else:
            r=sys.maxsize
            for i in l:
                if i<=n:
                    r=min(r,1+td(n-i,l))
    d[n]=r
    print(d)
    return r

def bu(n,l):
    for i in range(1,n+1):
        d[i]=sys.maxsize
    for value in range(1,n+1):
        for x in l:
            if x<=value:
                s=d[value-x]
                if s+1<d[value]:
                    d[value]=s+1
    print(d)
    return d[n]
            


if __name__=="__main__":
    
    l=eval(input())
    n=int(input())
    import timeit
    start=timeit.default_timer()
    print(bu(n,l))
    end=timeit.default_timer()
    print(end-start)