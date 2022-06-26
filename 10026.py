import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n = int(input())

board = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count_red, count_green, count_blue, count = 0, 0, 0, 0
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


def dfs(y, x, color):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if is_valid_coord(ny, nx) and not visited[ny][nx] and board[ny][nx] in color:
            visited[ny][nx] = True
            dfs(ny, nx, color)


for i in range(n):
    for j in range(n):
        if board[i][j] == 'R' and not visited[i][j]:
            dfs(i, j, 'R')
            count_red += 1

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G' and not visited[i][j]:
            dfs(i, j, 'G')
            count_green += 1
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'B' and not visited[i][j]:
            dfs(i, j, 'B')
            count_blue += 1
colors={'R','G'}
for i in range(n):
    for j in range(n):
        if board[i][j] in colors and not visited[i][j]:
            dfs(i, j, colors)
            count += 1

print(count_red + count_green + count_blue, count + count_blue)
