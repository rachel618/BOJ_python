n=int(input())
num=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
maxValue=-1e9
minValue=1e9
def dfs(index,result):
    global add,sub,mul,div,maxValue,minValue
    if index == n:
        maxValue=max(maxValue,result)
        minValue=min(minValue,result)
    else:
        if add>0:
            add-=1
            dfs(index+1,result+num[index])
            add+=1
        if sub>0:
            sub-=1
            dfs(index+1,result-num[index])
            sub+=1
        if mul>0:
            mul-=1
            dfs(index+1,result*num[index])
            mul+=1
        if div>0:
            div-=1
            dfs(index+1,int(result/num[index]))
            div+=1
dfs(1,num[0])
print(maxValue)
print(minValue)