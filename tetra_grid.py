# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:40:33 2020

@author: Harsh Sharma
"""
max1=int(input())-1
def grid(m,n):
    if m!=max1 or n!=max1:
        print('({},{})->'.format(m,n),end='')    
    if m==max1 and n==max1:
        print('({},{})'.format(m,n))
        return 1
    elif m==max1:        
        tmp=grid(max1,n+1)
        return tmp
    elif n==max1:
        tmp=grid(m+1,max1)
        return tmp
    else:
        tmp=grid(m+1,n)+grid(m,n+1)
        return tmp
    
print(grid(0,0))