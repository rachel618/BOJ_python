n=int(input())
board=[input() for _ in range(n)]
visited=[[False]*n for _ in range(n)]
ans=[]
dy=(0,1,0,-1)
dx=(1,0,-1,0)


def is_valid_coord(y,x):
    return 0 <= y < n and 0 <= x < n

def dfs(y,x):
    visited[y][x]=True
    global cnt
    stack=[]
    stack.append((y,x))
    while stack:
        y,x=stack.pop()
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if is_valid_coord(ny,nx) and not visited[ny][nx] and board[ny][nx]=='1':
                cnt=cnt+1
                visited[ny][nx]=True
                stack.append((ny,nx))

for y in range(n):
    for x in range(n):
        chk = False
        cnt=1
        count = 0
        if board[y][x]=='1' and not visited[y][x]:
            dfs(y,x)
            ans.append(cnt)
ans=sorted(ans,reverse=False)
print(len(ans))
print(*ans,sep='\n')
