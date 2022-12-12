import sys
import re
import operator
import math
import functools
input = sys.stdin.read().strip().split("\n\n")
monkeys = []
for ml in input:
    lines = list(map(lambda x: x.strip(), ml.split("\n")))
    monkey = {}
    monkeys.append(monkey)
    monkey["items"] = list(map(int,lines[1][len("Starting items: "):].split(",")))
    monkey["operation"] = lines[2][len("Operation: "):]
    monkey["test"] = int(lines[3][len("Test: divisible by "):])
    monkey["t"] = int(lines[4][len("If true: throw to monkey "):])
    monkey["f"] = int(lines[5][len("If false: throw to monkey "):])
    monkey["c"] = 0
lol = math.lcm(*[x["test"] for x in monkeys])
for _ in range(10000):
    for m in monkeys:
        for item in m["items"]:
            m["c"] += 1
            new = 0
            old = item
            exec(m["operation"])
            #new //= 3
            new %= lol;
            if new%m["test"] == 0:
                monkeys[m["t"]]["items"].append(new)
            else:
                monkeys[m["f"]]["items"].append(new)
        m["items"] = []
print(functools.reduce(operator.mul, sorted([x["c"] for x in monkeys])[-2:]))
