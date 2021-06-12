#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:47:51 2019

@author: root
"""



def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)


    
i=0
str1=''
def itfact(n):
    facty=1
    for i in range(2,n+1):
        facty*=i
    return facty
    
def fab(n):
    a=0
    b=1
    sum1=0
    while a<=n:
        sum1+=a
        s=a+b
        a=b
        b=s
    return sum1
        
def rfab(n):
    if n==0 or n==1:
        return n
    else:
        return rfab(n-1)+rfab(n-2)
    
    
    
def strrev(n):
    if len(n)==0:
        return n
    return strrev(n[1:])+n[0]

def itstr(n):
    s=''
    for i in range(1,len(n)+1):
        s=s+n[-i]
    return s
d={}
d[0]=0
d[1]=1
def rfib(n):
    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]
    
td={}
td[0]=0
td[1]=1
def tdfib(n):
    try:
        if td.get(n,-1)==-1:
            td[n]=tdfib(n-1)+tdfib(n-2)
    except:
        return td[n]
    return td[n]

def tdfib1(n):
    if td.get(n,-1)!=-1:
        return td[n]
    else:
        td[n]=tdfib1(n-1)+tdfib1(n-2)
        return td[n]

if __name__=='__main__':
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(tdfib1(n))
    end=timeit.default_timer()
    print("Time: ",end-start)
    
    