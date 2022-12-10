import sys
input = sys.stdin.read().strip().split("\n")
for Q in range(9):
    H = [0,0]
    T = [0,0]
    vis = set()
    vis.add(tuple(T))
    new_input = []
    for line2 in input:
        new_line = []
        for line in line2.split("#"):
            d,c = line.split()
            for _ in range(int(c)):
                if d == 'R':
                    H[1] += 1
                elif d == 'L':
                    H[1] -= 1
                elif d == 'U':
                    H[0] += 1
                elif d == 'D':
                    H[0] -= 1
                if "#" not in line2:
                    if H[0] < T[0] and abs(H[0]-T[0]) > 1 and H[1] == T[1]:
                        T[0] -= 1
                        new_line.append("D 1")
                    if H[1] > T[1] and  abs(H[1]-T[1]) > 1 and H[0] == T[0]:
                        T[1] += 1
                        new_line.append("R 1")
                    if H[0] > T[0] and  abs(H[0]-T[0]) > 1 and H[1] == T[1]:
                        T[0] += 1
                        new_line.append("U 1")
                    if H[1] < T[1] and  abs(H[1]-T[1]) > 1 and H[0] == T[0]:
                        T[1] -= 1
                        new_line.append("L 1")
                    if abs(H[0]-T[0])+abs(H[1]-T[1]) > 2:
                        if H[0] > T[0]:
                            T[0] += 1
                            new_line.append("U 1")
                        if H[0] < T[0]:
                            T[0] -= 1
                            new_line.append("D 1")
                        if H[1] > T[1]:
                            T[1] += 1
                            new_line.append("R 1")
                        if H[1] < T[1]:
                            T[1] -= 1
                            new_line.append("L 1")
                    vis.add(tuple(T))
                    if len(new_line) > 0:
                        new_input.append("#".join(new_line))
                        new_line = []
        if "#" in line2:
            if H[0] < T[0] and  abs(H[0]-T[0]) > 1 and H[1] == T[1]:
                T[0] -= 1
                new_line.append("D 1")
            if H[1] > T[1] and  abs(H[1]-T[1]) > 1 and H[0] == T[0]:
                T[1] += 1
                new_line.append("R 1")
            if H[0] > T[0] and  abs(H[0]-T[0]) > 1 and H[1] == T[1]:
                T[0] += 1
                new_line.append("U 1")
            if H[1] < T[1] and  abs(H[1]-T[1]) > 1 and H[0] == T[0]:
                T[1] -= 1
                new_line.append("L 1")
            if abs(H[0]-T[0])+abs(H[1]-T[1]) > 2:
                if H[0] > T[0]:
                    T[0] += 1
                    new_line.append("U 1")
                if H[0] < T[0]:
                    T[0] -= 1
                    new_line.append("D 1")
                if H[1] > T[1]:
                    T[1] += 1
                    new_line.append("R 1")
                if H[1] < T[1]:
                    T[1] -= 1
                    new_line.append("L 1")
            vis.add(tuple(T))
            if len(new_line) > 0:
                new_input.append("#".join(new_line))
    input = new_input
    if Q == 8:
        print(len(vis))
