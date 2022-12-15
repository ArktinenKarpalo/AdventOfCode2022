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
y = 2000000
for x in range(-6000000, 6000000):
    sk = False
    for s in sensors:
        if x == s[2] and y == s[3]:
            sk = True
            break
    if sk:
        continue
    for s in sensors:
        if dist(x, y, *s[:2]) <= dist(*s):
            ans += 1
            break

    
print(ans)

