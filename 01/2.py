import sys

input = [sum(x) for x in [map(int, x.split("\n")) for x in sys.stdin.read().strip().split("\n\n")]]
input = sorted(input)
print(sum(input[-3:]))
