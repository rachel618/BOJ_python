import sys

N=int(input())
for _ in range(N):
    str=sys.stdin.readline()
    sum,score=0,0
    for a in str:
        if a == "O":
            score=score+1
        else:
            sum+=score*(score+1)/2
            score=0
    print(int(sum))