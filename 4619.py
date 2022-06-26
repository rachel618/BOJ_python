import sys

while True:
    B,N=map(int,sys.stdin.readline().split())
    if B==0 or N==0: break
    n=int(B ** (1.0 / N))
    if abs(n**N-B) < abs((n+1)**N-B):
        print(n)
    else:
        print(n+1)