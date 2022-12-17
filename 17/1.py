import sys
input = sys.stdin.read().strip()
qq = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (0,1), (1,1), (2,1), (1, 2)],
    [(2,2), (2,1), (2,0), (0,0), (1, 0)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (0,1), (1,0), (1,1)]
]
sto = set()
def oob(x, y, r):
    for X,Y in r:
        if x+X <= 0 or x+X > 7:
            return True
        if y+Y <= 0:
            return True
        if (x+X, y+Y) in sto:
            return True
    return False
pt1 = 0
for i in range(2022):
    x = 3
    y = 0
    for X,Y in sto:
        y = max(y, Y)
    y += 4
    q = qq[i%len(qq)]
    while True:
        if input[pt1] == '>':
            if not oob(x+1, y, q):
                x+=1
        else:
            if not oob(x-1, y, q):
                x+=-1
        pt1 = (pt1+1)%len(input)
        if not oob(x, y-1, q):
            y -= 1
        else:
            for X,Y in q:
                sto.add((x+X,y+Y))
            break
ans = 0
for X,Y in sto:
    ans = max(ans, Y)

print(ans)
