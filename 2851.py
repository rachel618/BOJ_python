import sys

arr=[int(sys.stdin.readline()) for _ in range(10)]
absolute=[]
sum=0

for i in range(10):
    sum+=arr[i]
    arr[i]=sum
    absolute.append(abs(sum-100))
answer=list(filter(lambda x: arr[x]==absolute.index(min(absolute)), range(len(arr))))
print(answer)
print(arr[answer[-1]])





