import sys
import collections
import re
input = sys.stdin.read().strip().split("\n")[:3]

bst = collections.defaultdict(lambda: [])

def aa(cst, ore_robot, clay_robot, obs_robot, geo_robot, ore, clay, obs, geo, time):
    if time == 0:
        return geo
    for x in bst[(ore_robot,clay_robot,obs_robot,geo_robot,time)]:
        if ore <= x[0] and clay <= x[1] and obs <= x[2] and geo <= x[3]:
            return 0
    bst[(ore_robot,clay_robot,obs_robot,geo_robot,time)].append((ore,clay,obs,geo))
    rt = geo
    b=rt
    if ore >= cst[5] and obs >= cst[6]:
        b=aa(cst, ore_robot, clay_robot, obs_robot, geo_robot+1, ore+ore_robot-cst[5], clay+clay_robot, obs+obs_robot-cst[6], geo+geo_robot, time-1)
        rt = max(b, rt)
        return rt
    if ore >= cst[3] and clay >= cst[4]:
        b=aa(cst, ore_robot, clay_robot, obs_robot+1, geo_robot, ore+ore_robot-cst[3], clay-cst[4]+clay_robot, obs+obs_robot, geo+geo_robot, time-1)
        rt = max(b, rt)
    if ore >= cst[1] and ore_robot > -1:
        b = aa(cst, ore_robot+1, clay_robot, obs_robot, geo_robot, ore-cst[1]+ore_robot, clay+clay_robot, obs+obs_robot, geo+geo_robot, time-1)
    rt = max(b, rt)
    if ore >= cst[2] and clay_robot > -1:
        b=aa(cst, ore_robot, clay_robot+1, obs_robot, geo_robot, ore-cst[2]+ore_robot, clay+clay_robot, obs+obs_robot, geo+geo_robot, time-1)
    rt = max(b, rt)
    b=aa(cst, ore_robot, clay_robot, obs_robot, geo_robot, ore+ore_robot, clay+clay_robot, obs+obs_robot, geo+geo_robot, time-1)
    rt = max(b, rt)
    return rt

ans = 1
for line in input:
    m = re.match("Blueprint (.*): Each ore robot costs (.*) ore. Each clay robot costs (.*) ore. Each obsidian robot costs (.*) ore and (.*) clay. Each geode robot costs (.*) ore and (.*) obsidian.", line)
    cst = list(map(int, m.groups()))
    bst.clear()
    q = aa(cst,1,0,0,0,0,0,0,0,32)
    print(q)
    ans *= q
print(ans)
