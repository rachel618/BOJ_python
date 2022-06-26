import sys
input=sys.stdin.readline
n=int(input())
cnt=0
for _ in range(n):
    s=input().rstrip()
    stk=[]

    for i in range(len(s)):
        if stk and s[i]==stk[-1]:  # not empty & top==s[i]
            stk.pop()
        else:
            stk.append(s[i])
    if not stk:
        cnt+=1  # empty 이면 좋은 단어
print(cnt)