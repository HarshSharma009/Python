#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:50:28 2019

@author: root
"""


 
def printAllKLength(set, k): 

	n = len(set) 
	printAllKLengthRec(set, "", n, k) 


def printAllKLengthRec(set, prefix, n, k): 
    if (k == 0):
        	print(prefix)
        	return
    for i in range(n): 
        	newPrefix = prefix + set[i] 
        	printAllKLengthRec(set, newPrefix, n, k - 1) 

if __name__ == "__main__": 
	
	print("First Test") 
	set1 = ['a', 'b']
	k = 5
	printAllKLength(set1, k) 
	
	print("\nSecond Test") 
	set2 = ['a', 'b', 'c', 'd'] 
	k = 1
	printAllKLength(set2, k) 
 
