#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:11:24 2019

@author: root
"""

def assorted(n):
    l=[]
    s=[x for x in n] 
    s=list(set(s))
    for i in s:
        if n.count(i) in l:
            return False
        else:
            l.append(n.count(i))
    return True
def diverse(n):
    if assorted(n[:2]) and assorted(n[-2:]):
        print('It is diverse string')
    else:
        print('Not a diverse string')


if __name__=='__main__':
    n=input()
    check=assorted(n)
    print('assorted: ',check)
    if check:
        diverse(n)
    else:
        print('not a diverse string')
    