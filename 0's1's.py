'''
author: Harsh Sharma
'''



n=[0,0,1,0,0]
n=[-1 if i==0 else 1 for i in n]
sum1=0;ans=-1999;d={}
for index,i in enumerate(n):
    sum1+=i
    if sum1==0:
        ans=max(ans,index+1)
    if sum1 in d:
        ans=max(ans,index-d[sum1])
    else:
        d[sum1]=index;
    print(sum1,i,d,index)
print(ans)



    