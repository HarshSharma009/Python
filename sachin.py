#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:04:34 2019

@author: root
"""
ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]
twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]
thousands = ["","thousand ","million ", "billion ", "trillion "]
    
     
def num999(n):
    c = n % 10 # single digit ke liye
    b = ((n % 100) - c) // 10 # tens ke liye
    a = ((n % 1000) - (b * 10) - c) //100 # hundreds ke liye
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[a] + "hundred "
    elif a!=0:
        t = ones[a] + "hundred and "
    if b <= 1:
        h = ones[n%100]
    elif b > 1:
        h = twenties[b] + ones[c]
    st = t + h
    return st
     
def num2word(num):
    if num == 0: return 'zero'
    i = 3
    n = str(num)
    word = ""
    k = 0
    while(i == 3):
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word
        if n == '':
            i = i+1
        k += 1
    return word[:-1]
        

def isword(n,m):
    
    for i in range(len(n)):
        if n[i]<m[i]:
            return 1
        elif n[i]>m[i]:
            return 0
    if len(n)<len(m):
        return 1

def solve(n,m):
    flag=0
    while n!=m:
        f=num2word(n)
        s=num2word(m)
        #print(n,m)
        if isword(f,s):
            n+=n
            m+=m
        else:
            tmp=n
            n+=m
            m+=tmp
        if n>99900 or m>99900:
            flag=1
            break
        print(n,m)
    if flag==0:
        return n
    else:
        return 'no'


if __name__=='__main__':
    
    n,m=[int(x) for x in input().split()]
    print(solve(n,m))