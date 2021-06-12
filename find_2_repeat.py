for _ in range(int(input())) :
    n = int(input())
    arr = list(map(str,input().strip().split()))
    d=dict.fromkeys(arr,0)
    for i in arr:
        d[i]+=1
    d=sorted(d,key=d.get)
    print(d[-2])