import sys
input = sys.stdin.read().strip().split("\n")
ans = 0
for a, b in map(lambda x: x.split(), input):
    if b == 'X':
        if a == 'A':
            ans += 3
        elif a == 'B':
            ans += 0
        elif a == 'C':
            ans += 6
        ans += 1
    elif b == 'Y':
        if a == 'A':
            ans += 6
        elif a == 'B':
            ans += 3
        elif a == 'C':
            ans += 0
        ans += 2
    elif b == 'Z':
        if a == 'A':
            ans += 0
        elif a == 'B':
            ans += 6
        elif a == 'C':
            ans += 3
        ans += 3

print(ans)

