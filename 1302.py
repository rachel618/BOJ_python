n=int(input())
books=dict()

for _ in range(n):
    s=input()
    if s in books :
        books[s]+=1
    else:
        books[s]=1
sortedBooks=sorted(books.items(),key=lambda x: (-x[1],x[0]),reverse=False)
print(sortedBooks[0][0])