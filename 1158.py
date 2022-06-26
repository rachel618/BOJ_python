from collections import deque

n,k=map(int,input().split())
circle=deque([i for i in range(1,n+1)])
ans=[]
for i in range(1,n+1):
    circle.rotate(-k+1)
    ans.append(str(circle[0]))
    circle.remove(circle[0])
print("<"+', '.join(ans)+">")
