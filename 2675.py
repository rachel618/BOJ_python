import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N,str=sys.stdin.readline().strip().split()
    N=int(N)
    for a in str:
        for _ in range(N):print(a,end="")
    print()
