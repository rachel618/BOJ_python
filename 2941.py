import sys
word=["c=","c-","dz=","d-","lj","nj","s=","z="]
s=sys.stdin.readline().strip()
for a in word:
    s=s.replace(a,"1")
print(len(s))