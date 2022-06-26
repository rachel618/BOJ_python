import sys
arr=[int(sys.stdin.readline()) for _ in range(3)]
mul=str(arr[0]*arr[1]*arr[2])
for i in range(10):
    print(mul.count(f'{i}'))