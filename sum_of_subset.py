# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:46:06 2020

@author: Harsh Sharma
"""
l=list(map(int,input().split()))
tar=int(input())
n=len(l)
import itertools
import operator
from functools import reduce

'''Using of package creating combination with 1 to N(len of array)
and then checking for sum of subset is equal to target num'''
def sumofsubsetpack(array, num):
    subsets = reduce(operator.add, [list(itertools.combinations(array, r)) for r in range(1, 1 + len(array))])
    return [subset for subset in subsets if sum(subset) == num]
print(sumofsubsetpack(l,tar))

'''General approach of backtracking for finding sum of subset'''
tmp=[]
def isSubsetSum(set, n, sum,tmp) : 
    
    
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        
        return False
   
    
    if (set[n - 1] > sum) : 
        return isSubsetSum(set, n - 1, sum,tmp); 
    
    if isSubsetSum(set, n-1, sum,tmp)==True:
       
        return True
    if isSubsetSum(set, n-1, sum-set[n-1],tmp)==True:
        tmp.append(set[n-1])
        return True

#For less len of subset
if (isSubsetSum(l, n, tar,tmp) == True):
    print("Found a subset of sum {}:{}".format(tar,tmp))
else:
    print("No subset with given sum")

'''For Finding first subset which sum is equal to target num'''
def sumofsubset(l, num,n):
    
    if n == 0:
        return None
    else:
        if l[0] == num:
            return [l[0]]
        else:
            with_v = sumofsubset(l[1:], (num - l[0]),n-1)
            if with_v:
                return [l[0]] + with_v
            else:
                return sumofsubset(l[1:], num,n-1)  
print(sumofsubset(l,tar,n))

'''It will generate the list of tuple the tuple contain subset which sum
is equal to target num'''          
            
def sumofsubsetgenerator(array, num):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return
    for solution in sumofsubsetgenerator(array[1:], num):
        yield solution
    for solution in sumofsubsetgenerator(array[1:], num - array[0]):
        yield [array[0]] + solution
        
print(list(sumofsubsetgenerator(l,tar)))




def count(x, larger_than):
  if x == 0:
    return 1
  return sum(count(x - i ** N, i) for i in range(larger_than + 1, math.ceil(math.pow(x + 1, 1 / N))))


