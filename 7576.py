m,n=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

def is_valid_record(y,x):
    return 0<=y<n and 0<=x<m
def bfs():
