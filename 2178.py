from collections import deque

n, m = map(int, input().split())

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
board = [input() for _ in range(n)]


def bfs():
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    path = deque()
    path.append((0, 0, 1))
    while path:
        y, x, cnt = path.popleft()

        if y == n - 1 and x == m - 1:
            return cnt

        cnt = cnt + 1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx] == '1':
                visited[ny][nx] = True
                path.append((ny, nx, cnt))

print(bfs())
