import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
m,n,k=map(int,input().split())
board=[[0]*n for _ in range(m)]
visited=[[False]*n for _ in range(m)]

dx=(0,1,0,-1)
dy=(1,0,-1,0)
ans=[]

def is_valid_coord(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    global cnt
    visited[y][x]=True
    if board[y][x]==0:
        cnt+=1
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if is_valid_coord(nx,ny) and not visited[ny][nx] and board[ny][nx]==0:
            dfs(nx,ny)


for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[j][i]=1
cnt=0
for i in range(m):
    for j in range(n):
        if board[i][j]==0 and not visited[i][j]:
            dfs(j,i)
            ans.append(cnt)
            cnt=0
ans.sort()
print(len(ans))
print(*ans)



