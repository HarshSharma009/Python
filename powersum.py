# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:48:59 2020

@author: Harsh Sharma
"""

import math
n, N = int(input()), int(input())


c=0
def powersum(n,sum1):
    global c
    if n==0:
        return True
    else:
        for i in range(sum1+1,math.ceil(math.pow(n+1,1/N))):
            if powersum(n-i**N,i)==True:
                c+=1
powersum(n, 0)
print(c)