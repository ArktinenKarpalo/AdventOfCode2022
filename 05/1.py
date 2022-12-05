import sys
import re
input = sys.stdin.read().split("\n")
crates = [[] for _ in range(9)]
print(crates)
for line in input:
    if "[" in line:
        print(line)
        for i in range(9):
            if line[1+4*i] != ' ':
                crates[i].append(line[1+4*i])
    if " 1   2   3   4   5   6   7   8   9" in line:
        for idx,x in enumerate(crates):
            crates[idx] = list(reversed(x))
    if "move" in line:
        a, b, c = map(int, re.match("^move (.*) from (.*) to (.*)$", line).groups())
        b -= 1
        c -= 1
        for _ in range(a):
            crates[c].append(crates[b].pop())

for crate in crates:
    print(crate[-1], end="")
print()
