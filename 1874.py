n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        exit()

for i in answer:
    print(i)
