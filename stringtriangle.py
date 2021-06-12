#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:29:59 2019

@author: root
"""
s1="""A wiki is run using wiki software, otherwise known as a wiki engine.
 A wiki engine is a type of content management system,
 but it differs from most other such systems, including blog software,
 in that the content is created without any defined owner or leader, and wikis have little inherent structure,
 allowing structure to emerge according to the needs of the users.
 There are dozens of different wiki engines in use,
 both standalone and part of other software, such as bug tracking systems.
 Some wiki engines are open source, whereas others are proprietary.
 Some permit control over different functions (levels of access);
 for example, editing rights may permit changing, adding, or removing material.
 Others may permit access without enforcing access control.
 Other rules may be imposed to organize content. """
 
s="""much current research in artificial intelligence involves
designing programs that capture the knowledge and reasoning
processes of highly intelligent specialists. the practical goal of
such work is to make specialized expertise more generally
acecessible."""
l=s.split()
l.reverse()
tmp=[]
tmp.append(l[0])
i=1
s=l[i]

while True:
    
    if len(s)<=len(tmp[-1]):
        i+=1
        s=l[i]+' '+s
    elif len(s)>=len(tmp[-1]):
        tmp.append(s)
        i+=1
        s=l[i]
    if i>=len(l)-1:
        break
tmp[-1]=s+' '+tmp[-1] 
for i in range(len(tmp)-1,-1,-1):
    #print(len(tmp[i]))
    print(tmp[i])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
