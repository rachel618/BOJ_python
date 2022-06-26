import sys

s=sys.stdin.readline().strip()
s=list(s)
countZero=0
countOne=0
for i in range(0,len(s)-1):

    if s[i]=="1" and s[i+1]=="0":
        countOne=countOne+1
    elif s[i]=="0" and s[i+1]=="1":
        countZero=countZero+1
    if i+2 == len(s):
        if s[i+1]=="0" :
            countZero=countZero+1
        else:
            countOne=countOne+1
    else: continue
print(min(countOne,countZero))
