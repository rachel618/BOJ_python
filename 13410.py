import sys

N,K=map(int,sys.stdin.readline().split())
nums=[]
for i in range(1,K+1):
    tmp=list(str(N*i))
    tmp.reverse()
    num=int(''.join(tmp))
    nums.append(num)
print(max(nums))