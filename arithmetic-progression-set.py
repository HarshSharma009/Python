# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:54:22 2021

@author: abcd
"""

A=list(map(int,input().split()))
for j in range(1, len(A) - 1):
    i = j - 1
    k = j + 1
    while i >= 0 and k < len(A):
        if A[i] + A[k] == 2 * A[j]:
            print(A[i], A[j], A[k])
            k = k + 1
            i = i - 1
        elif A[i] + A[k] < 2 * A[j]:
            k = k + 1
        else:
            i = i - 1