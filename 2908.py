import sys

A,B=sys.stdin.readline().split()
A=A[::-1]
B=B[::-1]
if A<B: print(B)
else: print(A)
