import sys
from collections import deque
input=sys.stdin.readline
for _ in range(int(input())):
    count = 0
    n,m=map(int,input().split())
    priority=deque(map(int,input().split()))
    index=[0 for _ in range(n)]
    index[m]=1
    while True:
        if priority[0] == max(priority):
            count += 1
            if index[0] == 1:
                break
            else:
                priority.popleft()
                index.pop(0)
        else:
            priority.append(priority.popleft())
            index.append(index.pop(0))
    print(count)