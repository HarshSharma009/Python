"""
from itertools import permutations
tc=int(input())
for i in range(1,tc+1):
    count=0
    l=[]
    key=[]
    n,q=[int(x) for x in input().split()]
    
    for j in range(q):
        l.append([int(x) for x in input().split()])
    for j in permutations(l):
        tmp=[0]*(n+1)    
        avail=[]
        for k in j:
            s,e=k[0],k[1]
            count=0            
            for k in range(s,e+1):
                if tmp[k]==0:
                    tmp[k]=1
                    count+=1
            avail.append(count)
        key.append(min(avail))
    print('Case #{}: {}'.format(i,max(key)))    
"""
from collections import defaultdict as ddic
from collections import deque
from itertools import combinations, permutations, product
import bisect
from heapq import heappush, heappop, heapify
import sys
stdout = sys.stdout
rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split()))

def solve(N, Q, A):
    A.sort()
    OPEN, CLOSE = 0, 1
    events = []
    for i, (L, R) in enumerate(A):
        events.append((L, OPEN, i))
        events.append((R+1, CLOSE, i))
    
    events.sort()
    
    def possible(K):
        if K==0: return True
        banned = [False] * len(A)
        todo = len(A)
        while True:
            used = [0] * len(A)
            prev = None
            previ = None
            active = set()
            for X, cmd, i in events:
                if banned[i]: continue
                if prev is None:
                    prev = X
                #d = X - prev
                if len(active) == 1: # previous interval was 1
                    aa, = active
                    used[aa] += X - prev
                if cmd == OPEN:
                    active.add(i)
                else:
                    active.discard(i)
                prev = X
                #previ = i
                print(active)

            found = False
            for i in range(len(A)):
                if not banned[i] and used[i] >= K:
                    todo -= 1
                    found = True
                    banned[i] = True
                    if todo == 0: return True
            if not found: return False
            
            
            

    M = max(right - left + 1 for left, right in A)
    lo, hi = 0, M  #invariant poss(lo) is True
    while lo < hi:
        mi = (lo + hi + 1) // 2
        if possible(mi):
            lo = mi
        else:
            hi = mi - 1
            
    return lo
    
T = rri()
for tc in range(1, T+1):
    N, Q = rrm()
    queries = [rrm() for _ in range(Q)]
    ans = solve(N, Q, queries)
    print("Case #{}: {}".format(tc, ans))