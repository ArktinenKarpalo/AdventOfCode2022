import sys

input = [sum(x) for x in [map(int, x.split("\n")) for x in sys.stdin.read().strip().split("\n\n")]]
print(max(input))
