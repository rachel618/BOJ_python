import sys

T=int(sys.stdin.readline().strip())

if T%10 != 0:
    print(-1)
    exit()
A,B,C=0,0,0
while(True):
    if int(T/300) > 0:
        A = A + int(T / 300)
        T-=int(T/300)*300
    elif int(T/60) > 0:
        B = B + int(T / 60)
        T -= int(T/60)*60
    else:
        C=C+int(T/10)
        break
print(A,B,C)