# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:53:20 2020

@author: abcd
"""

import numpy as np
for _ in range(int(input())):
    n=int(input())
    mat=np.array(list(map(int,input().split()))).reshape(n,n)
    ans=np.rot90(mat,3)
    ans=ans.flatten()
    print(*ans)