
"""
Created on Tue Mar 10 13:26:01 2020

@author: Harsh Sharma
"""

def lcs(s1,s2):
    '''It is recursive way to find common string
    returns the largest common subsequence string'''
    if not s1 or not s2:
        return []
    x,xl,y,yl=s1[0],s1[1:],s2[0],s2[1:]
    if x==y:
        return [x]+lcs(xl,yl)
    else:
        return max(lcs(s1,yl),lcs(xl,s2),key=len)

def lcs2(x,y):
    '''It is a recursive method which takes an argument as length of a string'''
    if x<0 or y<0:
        return 0
    elif s1[x]==s2[y]:#if character matches then it will reduce the x,y both value
        return 1+lcs2(x-1,y-1)
    else:#if not then it will check both possibilities by reducing x,and after y
        return max(lcs2(x-1,y),lcs2(x,y-1))
    '''returs the length of largest common subsequence'''
    
def lcstd(x,y):
    '''Top down which takes an argument as length of a string'''
    if d.get((x,y),-1)!=-1:
        return d[(x,y)]
    if x<0 or y<0:
        result=0
    elif s1[x]==s2[y]:
        result = 1+lcs2(x-1,y-1)
    else:
        result= max(lcs2(x-1,y),lcs2(x,y-1))
    d[(x,y)]=result
    '''returns the length of the largest common subsequence'''
    return result
def lcsbu(l1,l2):
    '''Bottom Up method for LCS'''
    for i in range(l1+1):
        d[(0,i)]=0
    for i in range(l2+1):
        d[(i,0)]=0
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if s2[i-1]!=s1[j-1]:
                d[(i,j)]=max(d[(i-1,j)],d[(i,j-1)])
            else:
                d[(i,j)]=d[(i-1,j-1)]+1
    '''which returns the d[(len(s1),len(s2))] which is length of largest common subsequence'''
    return d[(i,j)]
    

def using_2D(l1,l2):
    '''Using 2-D array'''
    l=[[0 for _ in range(l1+1)] for _ in range(l2+1)]
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if s2[i-1]!=s1[j-1]:
                l[i][j]=max(l[i-1][j],l[i][j-1])
            else:
                l[i][j]=l[i-1][j-1]+1
    return l[i][j]
            
            
    
d={}      
s1='aaaaaaaaaaaaa'
s2='aaaaaaabcdjeihrc'
l1=len(s1);l2=len(s2)

import timeit
print('recursive time:')

print(timeit.timeit('print(lcs2(l1-1,l2-1))', globals=globals(), number=1))
print('topdown time:')

print(timeit.timeit('print(lcstd(l1-1,l2-1))', globals=globals(), number=1))
print('Bottomup time:')

print(timeit.timeit('print(lcsbu(l1,l2))', globals=globals(), number=1))
print(timeit.timeit('print(using_2D(l1,l2))', globals=globals(), number=1))

