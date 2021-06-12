# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:25:53 2021

@author: abcd
"""
import time
import timeit

setup_code = "from math import factorial"

statement = """
    for i in range(10):
        factorial(i)
"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 10000000)}")

n,k,m=map(int,input().split())
s=input()

start_time1 = time.time()

form=[]
i=0
j=k
while i<n:
    form.append(s[i:j])
    i+=k
    j+=k
l=list(form[0])
for i in range(1,len(form)):
    temp=[]
    for j in l:
        for k in form[i]:
            temp.append(j+k)
    l=temp
l=list(map(int,l))
print(sorted(l)[m-1])
print("--- %s seconds ---" % (time.time() - start_time1))


def Find_It(N, X, K, S):
    S = list(S)
    blocks = [S[i:i + X] for i in range(0, N, X)]
    digits = [sorted(set(i)) for i in blocks]
    freq = [len(x) for x in digits]
    for i in range(len(freq) - 2, -1, -1):
        freq[i] = freq[i] * freq[i + 1]
    if K > freq[0]:
        return -1
    freq.append(1)
    ans = []
    K = K - 1
    for i in range(1, len(freq)):
        div = K // freq[i]
        ans.append(digits[i - 1][div])
        K = K % freq[i]
    print(''.join(ans))
start_time = time.time()
Find_It(10,5,10,'1234567891')
print("--- %s seconds ---" % (time.time() - start_time))