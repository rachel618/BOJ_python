str=input()
stack=[]
numOfSticks=0
curSticks=0
ans=0
for ch in str:
    if ch=='(':
        numOfSticks=numOfSticks+1
        curSticks=curSticks+1

    else:  # ')'가 들어왔을 때
        if stack[-1] == '(':
            numOfSticks=numOfSticks-1
            curSticks=curSticks-1
            ans+=curSticks
        else:
            curSticks=curSticks-1

    stack.append(ch)
ans+=numOfSticks
print(ans)