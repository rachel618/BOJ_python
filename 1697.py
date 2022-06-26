from collections import deque

N,K=map(int,input().split())
visited = [False for _ in range(100001)]

def bfs(n,k):
    q=deque()
    q.append((n,0))
    visited[n]=True
    while q:
        now,sec=q.popleft()
        if now==k:
            return sec
        if now -1 >=0 and not visited[now-1]:
            q.append((now-1,sec+1))
            visited[now-1]=True
        if now +1 <=100000 and not visited[now+1]:
            q.append((now+1,sec+1))
            visited[now + 1] = True
        if 2*now <=100000 and not visited[now*2]:
            q.append((now*2,sec+1))
            visited[now * 2] = True


print(bfs(N,K))
