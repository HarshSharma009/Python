#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:06:53 2019

@author: root
"""

def box(m,n):
    
    if m==0 and n==0:
        return 1
    elif m==0:
        
        tmp=box(0,n-1)
        return tmp
    elif n==0:
        tmp=box(m-1,0)
        return tmp
    else:
        tmp=box(m-1,n)+box(m,n-1)
        return tmp
 
d={}
d[(0,0)]=1
def iboxpath(m,n):
    
    for r in range(1,n+1):
        d[(0,r)]=1
    for r in range(1,m+1):
        d[(r,0)]=1
    for r in range(1,m+1):
        for c in range(1,n+1):
            d[(r,c)]=d[(r-1,c)]+d[(r,c-1)]
            
            
    #for i in range(m,-1,-1):
        #for j in range(n,-1,-1):
            #print(d[(i,j)],end=' ')
        #print()
    return d[(m,n)]

def tdbox(m,n):
    if d.get((m,n),-1)!=-1:
        return d[(m,n)]
    else:
        if m==0 and n==0:
            return 1
        elif m==0:
            return box(0,n-1)
        elif n==0:
            return box(m-1,0)
        else:
            d[(m,n)]=box(m-1,n)+box(m,n-1)
            return d[(m,n)]
    
  
    
    
    
if __name__=="__main__":
    import timeit
    m=int(input())
    n=int(input())
    """
    print('Enter block box position: ')    
    i=int(input())
    j=int(input())
    

    start=timeit.default_timer()
    tmp=box(i,j)+box(m-i,n-j)
    tmp1=box(m,n)
    print(tmp1-tmp)
    end=timeit.default_timer()
    print("Time: ",end-start)
    """
    print(timeit.timeit('print(iboxpath(m-1,n-1))', globals=globals(), number=1))
    
    