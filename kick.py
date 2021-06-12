tc=int(input())
for j in range(1,tc+1):
    tmp=[]
    no,select=[int(x) for x in input().split()]
    l=[int(x) for x in input().split()]
    l=sorted(l,reverse=True)
    s,e=0,select
    tmp.append(sum(l[s+1:e]))
    s+=1
    e+=1
    while e<=no:
        tmp.append(tmp[-1]-l[s]+l[e-1])
        s+=1
        e+=1
    temp=(select-1)*l[0]-tmp[0]
    for i in range(1,len(tmp)):
        s=(select-1)*l[i]-tmp[i]
        if temp>s:
            temp=s
    
    print('Case #{}: {}'.format(j,temp))          
          
          
"""        
tc=int(input())
for j in range(1,tc+1):
    temp=0
    no,select=[int(x) for x in input().split()]
    l=[int(x) for x in input().split()]
    l=sorted(l,reverse=True)
    for i in range(1,select):
        temp+=(l[0]-l[i])
    start=1
    end=select+1
    while True:
        s=0
        if end>no:
            break
        for i in range(start,end):
            s+=(l[start]-l[i])
        if s<temp:
            temp=s
        
        start+=1
        end+=1
    print('Case #{}: {}'.format(j,temp))
"""