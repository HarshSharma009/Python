#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:40:59 2019

@author: root
"""

def myAtoi(s):
       try:
            if abs(int(s))<2147483648:
                return int(s)
            elif int(s)<0:
                return -2147483648
            else:
                return 2147483647
       except:            
           try:
               s=s.strip()
               if (s[0].isdigit() or s[0]=='-'):
                   tmp=''
                   if s[0]=='-':
                       tmp+='-'
                       s=s[1:]
                   elif s[0]=='+':
                       s=s[1:]
                   for i in s:
                       if i.isdigit():
                           tmp+=i
                       else:
                           break
                   if abs(int(tmp))<2147483648:
                       return int(tmp)
                   elif int(tmp)<0:
                       return -2147483648
                   else:
                       return 2147483647 
               else:
                   return 0
           except:
               return 0
           
print(myAtoi('  -0012a42'))