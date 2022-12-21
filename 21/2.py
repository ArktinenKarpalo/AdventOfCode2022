import sys
input = sys.stdin.read().strip().split("\n")

def lolasd(x):
    lol = {}
    while True:
        for line in input:
            a = line.split()
            a[0] = a[0][:-1]
            if len(a) == 2:
                if a[0] == 'humn':
                    lol[a[0]] = x
                else:
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
                        return lol[a[1]] >= lol[a[3]]
ans = 0
for i in range(60,0,-1):
    if lolasd(ans | (1<<i)):
        ans |= (1<<i)
print(ans)
