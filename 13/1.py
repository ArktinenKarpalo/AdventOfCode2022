import sys
input = sys.stdin.read().strip().split("\n\n")
def cmp(a, b):
    if type(a) == int and type(b) == int:
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
        return a <= b
    if type(a) == int:
        a = [a]
    if type(b) == int:
        b = [b]
    if len(a) == 0:
        if len(b) == 0:
            return 0
        else:
            return 1
    if len(b) == 0:
        return -1
    for x in range(max(len(a), len(b))):
        if len(a) == x:
            return 1
        elif len(b) == x:
            return -1
        res = cmp(a[x], b[x])
        if res != 0:
            return res
    return 0
ans = 0
for idx, pair in enumerate(input):
    a,b = pair.split("\n")
    exec(f"a = ({a})")
    exec(f"b = ({b})")
    if cmp(a, b) != -1:
        ans += idx+1
print(ans)
