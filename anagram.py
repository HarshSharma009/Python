#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:07:20 2019

@author: root
"""

# Python program to search all 
# anagrams of a pattern in a text 

MAX = 256


def compare(arr1, arr2): 
	for i in range(MAX): 
		if arr1[i] != arr2[i]: 
			return False
	return True
	
# This function search for all 
# permutations of pat[] in txt[] 
def search(pat, txt): 

	M = len(pat) 
	N = len(txt) 

	 
	countP = [0]*MAX

	countTW = [0]*MAX

	for i in range(M): 
		(countP[ord(pat[i]) ]) += 1
		(countTW[ord(txt[i]) ]) += 1

	# Traverse through remaining 
	# characters of pattern 
	for i in range(M, N): 

		# Compare counts of current 
		# window of text with 
		# counts of pattern[] 
		if compare(countP, countTW): 
			print("Found at Index", (i-M)) 

		# Add current character to current window 
		(countTW[ ord(txt[i]) ]) += 1

		# Remove the first character of previous window 
		(countTW[ ord(txt[i-M]) ]) -= 1
	
	# Check for the last window in text	 
	if compare(countP, countTW): 
		print("Found at Index", N-M) 
		
# Driver program to test above function	 
txt = "aabaabaa"
pat = "aaba"	
search(pat, txt) 

# This code is contributed 
# by Upendra Singh Bartwal 
