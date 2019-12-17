d={}	#using dictionary in top-down and in bottom-up method
d[(0,0)]=1 #Initializing with 1 for (0,0)th box is 1



#Recursive method

def box(m,n):
    if m==0 and n==0:
        return 1
    elif m==0:
        tmp=box(0,n-1)
        return tmp
    elif n==0:
        tmp=box(m-1,0)
        return tmp
    else:
        tmp=box(m-1,n)+box(m,n-1)
        return tmp

#top down approach

def tdbox(m,n):
    if d.get((m,n),-1)!=-1:
        return d[(m,n)]
    else:
        if m==0 and n==0:
            return 1
        elif m==0:
            return box(0,n-1)
        elif n==0:
            return box(m-1,0)
        else:
            d[(m,n)]=box(m-1,n)+box(m,n-1)
            return d[(m,n)]
    
  
#bottom up approach
def buboxpath(m,n):
    
    for r in range(1,n+1):
        d[(0,r)]=1
    for r in range(1,m+1):
        d[(r,0)]=1
    for r in range(1,m+1):
        for c in range(1,n+1):
            d[(r,c)]=d[(r-1,c)]+d[(r,c-1)]
    for i in range(m,-1,-1):
        for j in range(n,-1,-1):
            print(d[(i,j)],end=' ')
        print()
    return d[(m,n)]

    
    
    
if __name__=="__main__":
    import timeit
    m=int(input())
    n=int(input())
    print(timeit.timeit('print(box(m,n))', globals=globals(), number=1))     #time taken by recursive
    print(timeit.timeit('print(tdbox(m,n))', globals=globals(), number=1))   #time taken by top-down approach
    print(timeit.timeit('print(buboxpath(m,n))', globals=globals(), number=1))#time taken by bottom-up approach
    
    
