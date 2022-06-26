import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]

ans=[]
dx=(0,1,0,-1)
dy=(1,0,-1,0)

def is_valid_coord(y,x):
    return 0<=y<n and 0<=x<n
def bfs(y,x,h):
    visited[y][x]=True
    q=deque()
    q.append((y,x))
    while q:
        cur_y,cur_x=q.popleft()
        for d in range(4):
            nx=cur_x+dx[d]
            ny=cur_y+dy[d]
            if is_valid_coord(ny,nx) and board[ny][nx]>h and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((ny,nx))


for height in range(min(map(min,board)),max(map(max,board))):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[j][i]>height and not visited[j][i]:
                bfs(j,i,height)
                count=count+1
    ans.append(count)
print(max(ans))
