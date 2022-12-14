import sys
import math
input = sys.stdin.read().strip().split("\n")
lol = set()

max_y = 0
for line in input:
    crd = list(map(lambda x: list(map(int,x.split(","))), line.split("->")))
    for i in range(len(crd)-1):
        a = crd[i]
        b = crd[i+1]
        max_y = max(max_y, a[1], b[1])
        if a[0] == b[0]:
            for j in range(min(a[1], b[1]), max(a[1], b[1])+1):
                lol.add((a[0], j))
        else:
            for j in range(min(a[0], b[0]), max(a[0], b[0])+1):
                lol.add((j, a[1]))
line = f"-500,{max_y+2} -> 1000,{max_y+2}"
crd = list(map(lambda x: list(map(int,x.split(","))), line.split("->")))
for i in range(len(crd)-1):
    a = crd[i]
    b = crd[i+1]
    max_y = max(max_y, a[1], b[1])
    if a[0] == b[0]:
        for j in range(min(a[1], b[1]), max(a[1], b[1])+1):
            lol.add((a[0], j))
    else:
        for j in range(min(a[0], b[0]), max(a[0], b[0])+1):
            lol.add((j, a[1]))
sand_source = (500,0)
ans = 0
while True:
    cs = sand_source
    while True:
        if (cs[0], cs[1]+1) not in lol:
            cs = (cs[0], cs[1]+1)
        elif (cs[0]-1, cs[1]+1) not in lol:
            cs = (cs[0]-1, cs[1]+1)
        elif (cs[0]+1, cs[1]+1) not in lol:
            cs = (cs[0]+1, cs[1]+1)
        else:
            lol.add(cs)
            ans += 1
            if cs == sand_source:
                print(ans)
                exit(0)
            break
