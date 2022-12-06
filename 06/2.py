import sys
input = sys.stdin.read().strip()
for i in range(len(input)):
    if len(set(input[i:i+14]))==14:
        print(i+14)
        break
