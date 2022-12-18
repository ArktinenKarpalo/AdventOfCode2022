import sys
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
for line in input:
    a,b,c = map(int,line.split(","))
    for A,B,C in ofs:
        if (a+A, b+B, c+C) not in cb:
            ans += 1
print(ans)

