import heapq as hq

gifts=[]
N,M=map(int,input().split())
for i in map(int,input().split()):
    hq.heappush(gifts,-i)

ans=1
for child in map(int,input().split()):
    gift=-hq.heappop(gifts)
    if gift < child:
        ans=0
        break
    hq.heappush(gifts, -(gift - child))
print(ans)
