import sys
from collections import deque

N=int(sys.stdin.readline().strip())
dq=deque()
arr=[i for i in range(1,N+1)]
dq.extend(arr)
for _ in range(N-1):
    dq.popleft()
    tmp=dq.popleft()
    dq.append(tmp)
print(dq.pop())
