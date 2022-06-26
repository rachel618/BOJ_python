import heapq as hq
n,m=map(int,input().split())
gifts=[]

for i in map(int,input().split()):
    hq.heappush(gifts,-i)
for child in map(int,input().split()):
    g=-hq.heappop(gifts)
    if g>= child:
        hq.heappush(gifts,-(g-child))
    else:
        print("0")
        exit()
print("1")