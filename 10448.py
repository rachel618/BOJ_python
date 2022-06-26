import sys
from itertools import product

T = int(sys.stdin.readline().strip())
inputs = [int(sys.stdin.readline()) for _ in range(T)]

arr = [int(j * (j + 1) / 2) for j in range(1, 46)]

target = 0

def func(item):
    if item < target:
        return True
    else:
        return False

for i in range(T):
    isAnswer=False
    target = inputs[i]
    nums = list(filter(func, arr))
    for prod in product(nums,repeat=3):
        if sum(prod) == target:
            print(1)
            isAnswer=True
            break
    if isAnswer == False:
        print(0)
