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
pv = [0,0,0,0,0,0,0]
pvi = 0
i = -1
N = 1000000000000
tms = N//1725-2
LE = 0
LE = 2630*tms
N -= 1725*tms

i = -1
while i < N-1:
    i += 1
    x = 3
    y = 0
    for X,Y in sto:
        y = max(y, Y)
    y += 4
    q = qq[i%len(qq)]
    if pt1 == 0:
        aa = []
        aa2 = []
        for j in range(1, 7+1):
            a = 0
            for X,Y in sto:
                if X == j:
                    a = max(a, Y)
            aa.append(a)
            aa2.append(a-pv[j-1])
        print(i-pvi)
        pvi = i
        print(aa2)
        pv = aa
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
print(ans+LE)
