import sys
N = int(input())
XY = [sys.stdin.readline().split() for _ in range(N)]

sorted_XY = sorted(XY, key=lambda x: (int(x[0]), int(x[1])), reverse=False)

for i in sorted_XY:
    print(i[0], end=" ")
    print(i[1])

