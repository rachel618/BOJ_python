MOD=1_000_000_000
N=int(input())
dp=[[-1]*10 for _ in range(N+1)]
dp[1][0]=0
for i in range(1,10):
    dp[1][i]=1

def f(n,k):
    if dp[n][k]==-1 and n!=1:
        dp[n][k]=0
        if k==0:
            dp[n][k]=f(n-1,k+1)
        elif 1<=k<=8:
            dp[n][k]=f(n-1,k-1)+f(n-1,k+1)
        else:
            dp[n][k]=f(n-1,k-1)
    return dp[n][k]
sum=0
for j in range(10):
    f(N,j)
    sum+=dp[N][j]
print(sum%MOD)