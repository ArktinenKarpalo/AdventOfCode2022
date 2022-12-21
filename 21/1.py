import sys
input = sys.stdin.read().strip().split("\n")
lol = {}
while True:
    for line in input:
        a = line.split()
        a[0] = a[0][:-1]
        if len(a) == 2:
            lol[a[0]] = int(a[1])
        else:
            if a[1] in lol and a[3] in lol:
                if a[2] == '+':
                    lol[a[0]] = lol[a[1]]+lol[a[3]]
                elif a[2] == '-':
                    lol[a[0]] = lol[a[1]]-lol[a[3]]
                elif a[2] == '*':
                    lol[a[0]] = lol[a[1]]*lol[a[3]]
                elif a[2] == '/':
                    lol[a[0]] = lol[a[1]]/lol[a[3]]
                if a[0] == "root":
                    print(int(lol["root"]))
                    exit(0)
