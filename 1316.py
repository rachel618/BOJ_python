import sys
N=int(sys.stdin.readline().strip())

count=0
for _ in range(N):
    s=sys.stdin.readline().strip()
    visited = [0 for _ in range(26)]
    flag=True
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            continue
        else:
            if visited[ord(s[i])-ord('a')]==0:
                visited[ord(s[i])-ord('a')]=1
            else:
                break
                flag=False
    if visited[ord(s[len(s)-1])-ord('a')]==1:
        flag=False
    if flag == True:
        count=count+1
print(count)





