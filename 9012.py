import sys

for _ in range(int(sys.stdin.readline().strip())):
    st=[]
    isVPS=True
    for ch in sys.stdin.readline().strip():
        if ch=="(":
            st.append(ch)
        else: # ch==")"
            if st: # not empty
                st.pop()
            else:
                isVPS=False
                break
    if st:
        isVPS=False
    print("YES" if isVPS else "NO")
