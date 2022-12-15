import sys
import re
input = sys.stdin.read().strip().split("\n")
sensors = []
for line in input:
    asd = re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line)
    sensors.append(list(map(int, asd.groups())))
ans = 0
def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)
for y in range(0, 4000000+1):
    x = 0
    while x <= 4000000:
        sk = False
        mak = 0
        for s in sensors:
            if dist(x, y, *s[:2]) <= dist(*s):
                mak = max(mak, dist(*s)-dist(x, y, *s[:2]))
                sk = True
        if sk:
            x += max(mak-1, 1)
            continue
        print(x*4000000+y)
        exit(0)

