import sys
from itertools import combinations
N,M=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
min=sum(nums)
for combi in combinations(nums,3):
    if 0<=M-sum(combi)<min:
        min=M-sum(combi)
        answer=sum(combi)
print(answer)