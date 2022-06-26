import sys

N=int(sys.stdin.readline().strip())
for i in range(N):
    s=str(i)
    sum=i
    for a in s:
        sum+=int(a)
    if sum== N:
        print(i)
        exit()
print(0)