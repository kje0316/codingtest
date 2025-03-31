import sys
N = input()
N_list = sys.stdin.readline().split()
M = input()
M_list = sys.stdin.readline().split()

from collections import Counter
N_list = Counter(N_list)
for num in M_list:
    print(N_list[num],end=" " )