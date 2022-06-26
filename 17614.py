N=int(input())
cnt=0
for i in range(N+1):
    s = list(str(i))
    for a in s:
        if a in ['3','6','9']:
            cnt = cnt + 1

print(cnt)
