from collections import deque
deq=deque()

N,M=map(int,input().split())
pos=list(map(int,input().split()))

cnt=0
deq=deque([i for i in range(1,N+1)])
for i in pos:
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            if deq.index(i)<len(deq)/2:
                deq.append(deq.popleft())
                cnt+=1
            else:
                deq.appendleft(deq.pop())
                cnt+=1
print(cnt)
