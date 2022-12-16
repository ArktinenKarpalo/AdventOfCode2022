import sys
import re
import collections
input = sys.stdin.read().strip().split("\n")
valves = {}
lol = []
for line in input:
    asd = re.match("Valve (..) has flow rate=(.*); tunnels? leads? to valves?( .*,)* (..)", line)
    g = asd.groups()
    valve = {}
    valve["name"] = g[0]
    valve["flow"] = int(g[1])
    valve["dest"] = [g[3]]
    if g[2] != None:
        for x in g[2][:-1].strip().split(","):
            valve["dest"].append(x.strip())
    if valve["flow"] > 0:
        lol.append(g[0])
    valves[valve["name"]] = valve

dist = {}
for a in valves.values():
    for b in valves.values():
        if a == b:
            dist[(a["name"],b["name"])] = 0
        else:
            dist[(a["name"],b["name"])] = 1e9
for i in range(len(valves)):
    for a in valves.values():
        for b in valves.values():
            for d in b["dest"]:
                dist[(a["name"],d)] = min(dist[(a["name"],d)], dist[(a["name"],b["name"])]+1)
def h(cur, rem, sm, tkn):
    if rem <= 1:
        return -1
    cv = valves[cur]
    if cv["flow"] > 0:
        rem -= 1
        sm += rem*cv["flow"]
    ret = sm
    for i in lol:
        if i in tkn:
            continue
        tkn.add(i)
        ret = max(h(i, rem-dist[(cur, i)], sm, tkn), ret)
        tkn.remove(i)
    return ret

ans = h("AA", 30, 0, set())
print(ans)

