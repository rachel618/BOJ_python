N,A=map(int,input().split())
arr=list(map(int,input().split()))
def func(item):
    if item < A:
        return True
    else:
        return False
nums=list(filter(func,arr))
print(' '.join(map(str,nums)))