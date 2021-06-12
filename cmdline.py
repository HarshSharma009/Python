#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:44:50 2019

@author: root
"""
#import itertools
import sys
"""
l=sys.argv
l1=[]
for i in l[1:]:
    l1+=eval(i)
print(l1)
print(sorted(l1))
"""
print(sorted([int(j) for i in sys.argv[1:] for j in eval(i)]))
#print(sorted(itertools.chain(eval(sys.argv[1:]))))