point=[int(input()) for _ in range(2)]
if point[0]>0 and point[1]>0:
    print(1)
elif point[0] < 0 < point[1]:
    print(2)
elif point[0]<0 and point[1]<0:
    print(3)
else:
    print(4)