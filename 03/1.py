import sys
input = sys.stdin.read().strip().split("\n")
def prio(itm):
    if ord(itm) < ord('a'):
        return 1-ord('A')+ord(itm)+26
    else:
        return 1-ord('a')+ord(itm)
ans = 0
for s in input:
    st = set()
    for i in s[:len(s)//2]:
        st.add(i)
    for i in s[len(s)//2:]:
        if i in st:
            ans += prio(i)
            break
print(ans)

