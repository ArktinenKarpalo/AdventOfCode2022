import sys
input = sys.stdin.read().strip().split("\n")
cycle = 1
X = 1
cl = [20, 60, 100, 140, 180, 220, 1e9]
ans = 0
for line in input:
    a = line.split()
    if a[0] == "noop":
        cycle += 1
    elif a[0] == "addx":
        cycle += 1
        if cycle >= cl[0]:
            ans += cl[0]*X
            cl = cl[1:]
        X += int(a[1])
        cycle += 1
    if cycle >= cl[0]:
        ans += cl[0]*X
        cl = cl[1:]
print(ans)
