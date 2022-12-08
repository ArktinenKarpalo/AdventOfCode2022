import sys
input = sys.stdin.read().strip().split("\n")
vis = set()
for j in range(len(input[0])):
    d = -1
    for i in range(len(input)):
        q = int(input[i][j])
        if q > d:
            d = q
            vis.add((i,j))
    d = -1
    for i in range(len(input)-1, 0, -1):
        q = int(input[i][j])
        if q > d:
            d = q
            vis.add((i,j))
for i in range(len(input)):
    d = -1
    for j in range(len(input[i])):
        q = int(input[i][j])
        if q > d:
            d = q
            vis.add((i,j))
    d = -1
    for j in range(len(input[i])-1, 0, -1):
        q = int(input[i][j])
        if q > d:
            d = q
            vis.add((i,j))
print(len(vis))
