import sys
import collections
input = sys.stdin.read().strip().split("\n")
n = len(input)
m = len(input[1])
q = collections.deque()
vis = {}
for i in range(n):
    for j in range(m):
        if input[i][j] in ['S', 'a']:
            q.append((i,j))
            vis[(i,j)] = 0
def lvl(x, y):
    lvl = input[x][y]
    if lvl == 'S':
        lvl = 'a'
    elif lvl == 'E':
        lvl = 'z'
    lvl = ord(lvl)
    return lvl

while len(q) > 0:
    s = q.popleft()
    for ofs in [(1,0), (-1,0), (0, 1), (0,-1)]:
        c = (s[0]+ofs[0], s[1]+ofs[1])
        if c[0] < 0 or c[0] >= n:
            continue
        if c[1] < 0 or c[1] >= m:
            continue
        if lvl(*c) > lvl(*s)+1:
            continue
        if c in vis:
            continue
        vis[c] = vis[s]+1
        q.append(c)
    if input[s[0]][s[1]] == 'E':
        print(vis[s])
