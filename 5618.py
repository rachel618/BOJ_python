import sys
import math
N=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))
if len(arr)==2:
    num=math.gcd(arr[0],arr[1])
else:
    num=math.gcd(arr[0],arr[1],arr[2])

def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()
    return divisorsList
print(*getMyDivisor(num),sep="\n")