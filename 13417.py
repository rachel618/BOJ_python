T=int(input())
alphabets=[]
for _ in range(T):
    alphabets.clear()
    N=int(input())
    alphabets.extend(input().split())
    alphabets=sorted(alphabets,reverse=False)
    print(alphabets)



