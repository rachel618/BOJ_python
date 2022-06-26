import sys
from itertools import combinations

arr=[int(sys.stdin.readline().strip()) for _ in range(9)]

for combi in combinations(arr,7):
    if sum(combi) == 100:
        print(*combi, sep="\n")