import sys
input = list(map(int, sys.stdin.read().strip().split("\n")))
lol1 = list(range(1,len(input)))+[0]
lol2 = [len(input)-1]+list(range(len(input)-1))
K = 811589153
for _ in range(10):
    for idx,ofs in enumerate(input):
        ofs *= K
        ofs %= len(input)-1
        if ofs == 0:
            continue
        lol1[lol2[idx]] = lol1[idx]
        lol2[lol1[idx]] = lol2[idx]
        cur = idx
        if ofs > 0:
            for _ in range(ofs):
                cur = lol1[cur]
        elif ofs < 0:
            for _ in range(abs(ofs)+1):
                cur = lol2[cur]

        lol1[idx] = lol1[cur]
        lol2[idx] = cur

        lol2[lol1[cur]] = idx
        lol1[cur] = idx
ans = 0
cur = 0
for i in range(100000):
    cur = lol1[cur]
    if input[cur] == 0:
        break
for i in range(1,5000):
    cur = lol1[cur]
    if i in [1000, 2000, 3000]:
        ans += input[cur]*K
print(ans)
