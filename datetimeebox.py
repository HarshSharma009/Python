#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:55:19 2019

@author: root
"""

from datetime import datetime,timedelta
print('Enter the date as dd-mm-yyyy format:')
d=input()
print('Number of Data Sequences')
n=int(input())
print('Starting Date is :',d)
print('Next {} dates :'.format(n))
start=datetime(int(d[-4:]),int(d[3:5]),int(d[0:2]))
for i in range(n):
    #start=datetime(int(d[-4:]),int(d[3:5]),int(d[0:2]))
    new=start+timedelta(20)
    start=new
    print(str('{}-{}-{}'.format(new.day,new.month,new.year)))