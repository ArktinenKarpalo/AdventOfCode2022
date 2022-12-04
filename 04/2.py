import sys
input = sys.stdin.read().strip().split("\n")
ans = 0
for line in input:
    a,b = map(lambda x: x.split("-"), line.split(","))
    a = list(map(int, a))
    b = list(map(int, b))
    if a[0] > b[0]:
        a,b = b,a
    if b[0] <= a[1]:
        ans += 1
print(ans)

