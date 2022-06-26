import sys

n=int(sys.stdin.readline().strip())
entered={}
for _ in range(n):
    name,log=map(str,sys.stdin.readline().split())
    if log=="enter":
        entered[name]=1
    else:
        del entered[name]
entered=sorted(entered.keys(),reverse=True)
print(*entered,sep="\n")