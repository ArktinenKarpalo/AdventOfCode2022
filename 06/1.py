import sys
input = sys.stdin.read().strip()
for i in range(len(input)):
    if len(set(input[i:i+4]))==4:
        print(i+4)
        break
