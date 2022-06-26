import sys

while True:
    N,M=map(int,sys.stdin.readline().split())

    if N==0 and M==0:
        break
    s=set()
    for _ in range(N):
        s.add(int(sys.stdin.readline().strip()))

    ans=0
    for _ in range(M):
        if int(sys.stdin.readline().strip()) in s:
                ans+=1

    print(ans)