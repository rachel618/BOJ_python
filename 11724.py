import sys

input=sys.stdin.readline
n, m = map(int, input().split())
adj = [[0] * n for _ in range(n)]
visited = [False for _ in range(n)]
count = 0

def dfs(start_node):
    stack = []
    visited[start_node] = True
    stack.append(start_node)
    while stack:  # not empty 동안 반복
        cur_node = stack[-1]
        check = False
        for next_node in range(n):
            if not visited[next_node] and adj[cur_node][next_node] == 1:
                visited[next_node] = True
                stack.append(next_node)
                check = True
        if not check:
            stack.pop()


for _ in range(m):
    y, x = map(int, input().split())
    adj[y - 1][x - 1], adj[x - 1][y - 1] = 1, 1
for i in range(n):
    if not visited[i]:
        dfs(i)
        count = count + 1
print(count)
