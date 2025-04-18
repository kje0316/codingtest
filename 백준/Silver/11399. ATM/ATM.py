import sys
N = int(input())
time = list(map(int, input().split()))
time.sort()

t = 0
result = 0
for i in range(len(time)):
    t += time[i]
    result += t


print(result)