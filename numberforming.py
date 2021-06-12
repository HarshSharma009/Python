# -*- coding: utf-8 -*-
"""
Created on Thu May 20 23:13:15 2021

@author: Harsh Sharma
"""

n,x,k=map(int,input().split())
s = list(input())
digits = [sorted(set(i)) for i in [s[i:i + x] for i in range(0, n, x)]]
freq = [len(x) for x in digits]

for i in range(len(freq) - 2, -1, -1):
    freq[i] = freq[i] * freq[i + 1]
if k > freq[0]:
    print(-1)
else:    
    freq.append(1)
    ans = []
    k = k - 1
    for i in range(1, len(freq)):
        div = k // freq[i]
        ans.append(digits[i - 1][div])
        k = k % freq[i]
    print(''.join(ans))