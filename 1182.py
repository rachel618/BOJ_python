import sys
input=sys.stdin.readline
n,s=map(int,input().split())
nums=list(map(int,input().split()))
count=0
def func(index,sum):
    global count
    if index == len(nums):
        return
    sum+=nums[index]

    if sum == s:
        count=count+1

    func(index+1,sum)
    func(index+1,sum-nums[index])
count=0
func(0,0)
print(count)

