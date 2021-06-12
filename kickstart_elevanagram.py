T = int(input())
for iter in range(1, T+1):
    flag = True
    A = list(map(int, input().split(' ')))
    total = 0
    nums = []
    for i in range(9):
        nums += [i+1]*A[i]
        total += (i+1)*A[i]
    N = len(nums)
    if N&1:
        m = sum(nums[:(N+1)//2])-sum(nums[(N+1)//2:])
        M = sum(nums[(N-1)//2:])-sum(nums[:(N-1)//2])
    else:
        m = 0
        M = sum(nums[N//2:])-sum(nums[:N//2])
    for i in range(m, M+1):
        if i%11==0 and (total+i)%2==0:
            print("Case #{}: {}".format(iter, 'YES'))
            flag = False
            break
    if flag:
        print("Case #{}: {}".format(iter, 'NO'))