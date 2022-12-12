import sys
input = sys.stdin.read().strip().split("\n")
curpath = []
files = {}
dirs = set()

for line in input:
    if line.startswith("$"):
        p = line.split(" ")
        if p[1] == "ls":
            pass
        elif p[1] == "cd":
            if p[2] == '/':
                curpath = []
            elif p[2] == '..':
                curpath.pop()
            else:
                curpath.append(p[2])
    elif line.startswith("dir"):
        p = line.split(" ")
        dirs.add(f'{"/".join(curpath)}{"/" if len(curpath) > 0 else ""}{p[1]}')
    else:
        p = line.split(" ")
        files[f'{"/".join(curpath)}{"/" if len(curpath) > 0 else ""}{p[1]}'] = int(p[0])
ans = 0
for dir in dirs:
    sz = 0
    for path,size in files.items():
        if path.startswith(dir):
            sz += size
    if sz < 100000:
        ans += sz
print(ans)
