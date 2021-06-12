# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:45:06 2020

@author: abcd
"""

def maxDistance(arr, n):
    max1=0
    d={}
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]]=i
        elif max1<(i-d[arr[i]]):
            max1=i-d[arr[i]]
            
        
    return max1
