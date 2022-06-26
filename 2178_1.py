from collections import deque

n,m=map(int,input().split())
board=[input() for _ in range(n)]
visited=[[False] *m for _ in range(n)]
cnt=0
dx=(0,1,0,-1)
dy=(1,0,-1,0)

def is_valid_coord(y,x):
    return 0<=y<n and 0<=x<m

def bfs(y,x):
    q=deque()
    q.append((y,x,1))
    while q:
        now_y,now_x,cnt=q.popleft()

        if now_y ==n-1 and now_x ==m-1:
            return cnt
        for d in range(4):
            ny=now_y+dy[d]
            nx=now_x+dx[d]
            if is_valid_coord(ny,nx) and not visited[ny][nx] and board[ny][nx]=='1':
                visited[ny][nx]=True
                q.append((ny,nx,cnt+1))


print(bfs(0,0))


