T=int(input())
for _ in range(T):
    H,W,N=map(int,input().split())
    if N%H==0:
        h,w=H,int(N/H)
    else:
        h,w=N%H,int(N/H+1)
    print(f'{h}' + format(w,'02'))