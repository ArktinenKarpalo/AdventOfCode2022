import sys
input = sys.stdin.read().strip().split("\n")
cycle = 0
X = 1
ans = [['Q' for _ in range(40)] for _ in range(6)]
for line in input:
    a = line.split()
    if a[0] == "noop":
        y = cycle//40
        x = cycle%40
        if abs(X-x) <= 1:
            ans[y][x] = '#'
        else:
            ans[y][x] = '.'
        cycle += 1
    elif a[0] == "addx":
        y = cycle//40
        x = cycle%40
        if abs(x-X) <= 1:
            ans[y][x] = '#'
        else:
            ans[y][x] = '.'
        cycle += 1
        y = cycle//40
        x = cycle%40
        if abs(x-X) <= 1:
            ans[y][x] = '#'
        else:
            ans[y][x] = '.'
        X += int(a[1])
        cycle += 1
for x in ans:
    print("".join(x))
