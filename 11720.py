import sys

N=int(sys.stdin.readline())
str=sys.stdin.readline().strip()
sum=0
for a in str:
    sum+=int(a)
print(sum)