import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.read().strip().split("\n")
cb = set()
for line in input:
    a,b,c = map(int,line.split(","))
    cb.add((a,b,c))
ofs = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1]
]
ans = 0
vis = set()
def src(c1, c2, c3):
    if (c1,c2,c3) in vis:
        return
    if (c1,c2,c3) in cb:
        return
    vis.add((c1,c2,c3))
    if min(c1,c2,c3) < -1 or max(c1,c2,c3) > 22:
        return
    for C1,C2,C3 in ofs:
        src(c1+C1,c2+C2,c3+C3)
src(-1,-1,-1)
for line in input:
    a,b,c = map(int,line.split(","))
    for A,B,C in ofs:
        if (a+A, b+B, c+C) in vis:
            ans += 1
print(ans)

