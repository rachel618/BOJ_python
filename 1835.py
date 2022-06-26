n = int(input())
l = [n]
# 역순으로 수행해서 배열에 저장
for i in range(n-1,0,-1):
    l = [i]+l
    for j in range(i):
        temp = l[0:n-i]
        l = [l[n-i]] + temp
for i in range(n):
    print(l[i],end=' ')