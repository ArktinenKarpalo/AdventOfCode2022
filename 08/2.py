import sys
input = sys.stdin.read().strip().split("\n")
ans = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        cs = 1
        cr = 0
        for k in range(i+1, len(input)):
            cr += 1
            q = int(input[k][j])
            if q >= int(input[i][j]):
                break
        cs *= cr
        cr = 0
        for k in range(i-1, 0-1, -1):
            cr += 1
            q = int(input[k][j])
            if q >= int(input[i][j]):
                break
        cs *= cr
        cr = 0
        for k in range(j+1, len(input[i])):
            cr += 1
            q = int(input[i][k])
            if q >= int(input[i][j]):
                break
        cs *= cr
        cr = 0
        for k in range(j-1, 0-1, -1):
            cr += 1
            q = int(input[i][k])
            if q >= int(input[i][j]):
                break
        cs *= cr
        cr = 0
        ans = max(ans, cs)
print(ans)
