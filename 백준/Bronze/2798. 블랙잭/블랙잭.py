import sys
import itertools

N, M = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
combinations = list(itertools.combinations(list(range(N)), 3))
num = []
for a,b,c in combinations:
    num.append(numbers[a-1]+numbers[b-1]+numbers[c-1])
num.sort()
for n in range(len(num)): 
    if num[n] > M:
        print(num[n-1])
        break
if num[-1] < M:
    print(num[-1])