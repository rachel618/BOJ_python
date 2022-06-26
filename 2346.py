from collections import deque

n=int(input())
ans=[]

dq=deque()
dq.extend([i for i in range(n)])
arr=list(map(int,input().split()))  # 3 2 1 -3 -1
for _ in range(n):
    idx=dq.popleft()
    ans.append(str(idx+1))
    if arr[idx]>0:
        dq.rotate(-arr[idx]+1)
    else:
        dq.rotate(-arr[idx])

print(' '.join(ans))