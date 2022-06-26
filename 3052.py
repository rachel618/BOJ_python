import sys

arr=[int(sys.stdin.readline())%42 for _ in range(10)]
answer=[0 for _ in range(42)]

for i in range(10):
    answer[arr[i]]=1
def nonZero(item):
    if item>0:
        return True
    else:
        return False
answer=list(filter(nonZero,answer))
print(len(answer))