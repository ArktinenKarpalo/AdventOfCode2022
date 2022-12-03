import sys
input = sys.stdin.read().strip().split("\n")
def prio(itm):
    if ord(itm) < ord('a'):
        return 1-ord('A')+ord(itm)+26
    else:
        return 1-ord('a')+ord(itm)
ans = 0
for s in range(0, len(input), 3):
    ans += prio(list(set(list(input[s]))&set(list(input[s+1]))&set(list(input[s+2])))[0])
print(ans)

