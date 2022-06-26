N=int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    print(f'Case #{i+1}: {arr[i][0]} + {arr[i][1]} = {arr[i][0]+arr[i][1]}')
