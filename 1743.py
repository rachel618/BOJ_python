import sys

input=sys.stdin.readline

n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
start_nodes=[]
ans=[]
def is_valid_coord(y,x):
    return 0<=y<n and 0<=x<m

def dfs(y,x):
    path = []
    count=1
    visited[y][x] = True
    path.append((y,x))
    while path:  # not empty 동안 반복
        cur_y,cur_x = path.pop()

        for d in range(4):
            ny = cur_y + dy[d]  # next y, x
            nx = cur_x + dx[d]
            if is_valid_coord(ny,nx) and not visited[ny][nx] and board[ny][nx] == 1:
                visited[ny][nx] = True
                path.append((ny,nx))
                count=count+1
    return count


for _ in range(k):
    y,x=map(int,input().split())
    board[y-1][x-1]=1
    start_nodes.append((y-1,x-1))

for _ in range(k):
    y,x=start_nodes.pop()
    ans.append(dfs(y,x))
print(max(ans))

