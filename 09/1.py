import sys
input = sys.stdin.read().strip().split("\n")
print(input)
H = [0,0]
T = [0,0]
vis = set()
vis.add(tuple(T))
for line in input:
    d,c = line.split()
    for _ in range(int(c)):
        if d == 'R':
            H[1] += 1
            if abs(H[1]-T[1]) > 1 and H[0] == T[0]:
                T[1] += 1
        elif d == 'L':
            H[1] -= 1
            if abs(H[1]-T[1]) > 1 and H[0] == T[0]:
                T[1] -= 1
        elif d == 'U':
            H[0] += 1
            if abs(H[0]-T[0]) > 1 and H[1] == T[1]:
                T[0] += 1
        elif d == 'D':
            H[0] -= 1
            if abs(H[0]-T[0]) > 1 and H[1] == T[1]:
                T[0] -= 1
        if abs(H[0]-T[0])+abs(H[1]-T[1]) > 2:
            if H[0] > T[0]:
                T[0] += 1
            if H[0] < T[0]:
                T[0] -= 1
            if H[1] > T[1]:
                T[1] += 1
            if H[1] < T[1]:
                T[1] -= 1
        vis.add(tuple(T))

print(len(vis))
