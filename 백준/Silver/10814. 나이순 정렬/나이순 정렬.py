import sys
N = int(input()) #회원 수
T = [sys.stdin.readline().split() for _ in range(N)]

sorted_T = sorted(T, key=lambda x: int(x[0]), reverse = False)

for t in sorted_T:
    print(t[0], end=" ")
    print(t[1])         