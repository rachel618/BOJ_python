from itertools import combinations

arr=[int(input()) for _ in range(9)]

for combi in combinations(arr,7):
    if sum(combi) == 100:
        for i in combi:
            print(i)