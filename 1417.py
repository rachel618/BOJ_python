import sys
import heapq

N=int(sys.stdin.readline().strip())
dasom=int(sys.stdin.readline().strip())
votes=[]
for _ in range(N-1):
    n=int(sys.stdin.readline().strip())
    heapq.heappush(votes,-n)
cnt=0
while votes:
    tmp=-heapq.heappop(votes)
    if dasom>tmp:
        break
    dasom+=1
    cnt+=1
    heapq.heappush(votes,-(tmp-1))
print(cnt)