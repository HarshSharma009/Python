# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:17:38 2020

@author: Harsh Sharma
"""

def parenthesis_generator(openB,closeB,n,s=[]):
    if n==closeB:
        print(''.join(s))
        return
        
    else:
        if openB>closeB:
            s.append(')')
            parenthesis_generator(openB,closeB+1,n,s)
            s.pop()
        if openB<n:
            s.append('(')
            parenthesis_generator(openB+1,closeB,n,s)
            s.pop()
    return
        

parenthesis_generator(0,0,3)