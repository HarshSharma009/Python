# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:39:50 2020

@author: abcd
"""

import re
f1=open("input.txt","r")
f2=open('output.txt','w')
for line in f1:
    lis=re.findall('[789]\d{9}',line)
    for n in lis:
        f2.write(n+'\n')
print('Extracted all Mobile number')
f1.close()
f2.close()