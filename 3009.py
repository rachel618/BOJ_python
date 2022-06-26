arr=[list(map(int, input().split())) for _ in range(3)]
xs=[arr[i][0] for i in range(3)]
ys=[arr[i][1] for i in range(3)]
if xs.count(arr[0][0]) == 1:
    pos_x=arr[0][0]
elif arr[0][0]== arr[1][0]:
    pos_x=arr[2][0]
else:
    pos_x=arr[1][0]

if ys.count(arr[0][1]) == 1:
    pos_y=arr[0][1]
elif arr[0][1]== arr[1][1]:
    pos_y=arr[2][1]
else:
    pos_y=arr[1][1]

print(pos_x, pos_y)