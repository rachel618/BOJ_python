import sys
from collections import deque

input=sys.stdin.readline

dx=(-2,-1,1,2,2,1,-1,-2)
dy=(1,2,2,1,-1,-2,-2,-1)
def is_valid_coord(x,y,l):
    return 0<=x<l and 0<=y<l

def bfs(x,y,length):
    global dest_x,dest_y
    q=deque()
    q.append((x,y,0))
    visited[x][y]=True
    while q:
        now_x,now_y,count=q.popleft()
        if now_x == dest_x and now_y== dest_y:
            return count
        for d in range(8):
            nx=now_x+dx[d]
            ny=now_y+dy[d]
            if is_valid_coord(nx,ny,length) and not visited[nx][ny]:
                q.append((nx,ny,count+1))
                visited[nx][ny]=True


for _ in range(int(input())):
    l=int(input())
    now_x,now_y=map(int,input().split())
    dest_x,dest_y=map(int,input().split())
    visited=[[False]*l for _ in range(l)]
    print(bfs(now_x,now_y,l))