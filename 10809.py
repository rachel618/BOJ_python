import sys
str=sys.stdin.readline().strip()
alphabet=[-1 for _ in range(26)]
for a in str:
    alphabet[ord(a)-ord('a')]=str.index(a)
print(*alphabet)