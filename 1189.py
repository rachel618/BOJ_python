import sys

input=sys.stdin.readline
r,c,k=map(int,input().split())
board=[input().rstrip() for _ in range(r)]
visited=[[False]*c for _ in range(r)]

dx=(0,1,0,-1)
dy=(1,0,-1,0)

def is_valid_coord(y,x):
    return 0<=y<r and 0<=x<c

def dfs(y,x,count):
    global ans
    if count == k and y==0 and x==c-1:
        ans+=1
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if is_valid_coord(ny,nx) and not visited[ny][nx] and board[ny][nx]!='T':
            visited[ny][nx]=True
            dfs(ny,nx,count+1)
            visited[ny][nx]=False
ans=0
visited[r-1][0]=True
dfs(r-1,0,1)
print(ans)