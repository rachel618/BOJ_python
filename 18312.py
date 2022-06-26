import sys

N,K=map(int,sys.stdin.readline().split())
#
# if N<K or K==0: n=N+1
# elif N<10+K: n=N
# elif N<20+K: n=N-1
# else: n=N-2
# if K<6:
#     print((N+1)*60*60 - (n*45*45))
# else:
#     print((N+1)*60*60 - n*54*54)
count=0
h,m,s='','',''
for i in range(N+1):
    if i<10:
        h='0'+str(i)
    else:
        h=str(i)
    for j in range(60):
        if j<10:
            m='0'+str(j)
        else:
            m=str(j)
        for k in range(60):
            if k<10:
                s='0'+str(k)
            else:
                s=str(k)
            if str(K) in h or str(K) in m or str(K) in s: count+=1
print(count)