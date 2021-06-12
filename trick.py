# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:51:23 2020

@author: abcd
"""
'''Sorting based on value'''
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])

import operator
sorted(xs.items(), key=operator.itemgetter(1))
