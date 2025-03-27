import sys
N = int(input())
XY = [sys.stdin.readline().split() for _ in range(N)]

sorted_XY = sorted(XY, key=lambda x: (int(x[1]), int(x[0])), reverse=False)

for i in sorted_XY:
    print(i[0], end=" ")
    print(i[1])
