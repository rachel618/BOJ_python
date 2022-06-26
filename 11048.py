import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

def f(n,m):
    if n==0 and m==0:
        return arr[n][m]
    elif n==0 and m!=0:
        return f(n,m-1) + arr[n][m]
    elif n!=0 and m==0:
        return f(n-1,m) + arr[n][m]
    return max(f(n-1,m),f(n,m-1),f(n-1,m-1)) + arr[n][m]
print(f(N-1,M-1))