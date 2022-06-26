import sys
from itertools import combinations

arr=[int(sys.stdin.readline().strip()) for _ in range(9)]
for combi in combinations(arr,7):
    if sum(combi) == 100:
        combi=list(combi)
        combi.sort()
        print(*combi,sep="\n")
        break
# break 안넣어줘서 틀림