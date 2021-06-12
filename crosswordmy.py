# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:12:18 2020

@author: abcd
"""
l=['+-++++++++',
   '+-++++++++',
   '+-++++++++',
   '+-----++++',
   '+-+++-++++',
   '+-+++-++++',
   '+++++-++++',
   '++------++',
   '+++++-++++',
   '+++++-++++',
   '+++++-++++']

name=['LONDON','DELHI','ICELAND','ANKARA']
i=0
le=len(name)
l=[list(l[i]) for i in range(len(l))]
while i<le:
    tmp=0
    flag=False
    for j in range(len(l)):
        if '-' in l[j]:
            if l[j].count('-')>1:
                flag=True
                break
            else:
                flag=False
                break
    if flag:
        for k in range(len(l[i])):
            if l[j][k]=='-' or l[j][k].isalpha():
                l[j][k]=name[i][tmp]
                tmp+=1
        i+=1
        continue
    else:
        for k in range(len(l[j])):
            if '-'==l[j][k]:
                
                break
        print(j,k)
        for temp in range(j,len(name[i])+j):
            l[temp][k]=name[i][tmp]
            tmp+=1
        i+=1
    
                
                
            
    