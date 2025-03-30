import sys
N = int(input())

N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort() #1 2 3 4 5

M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))
answer = []
for M_num in M_list: 
    
    left, right = 0, len(N_list)-1  #0, 4
    found = False
    while left <= right:
        mid = (left + right)//2 #2
        if M_num == N_list[mid]: 
            print(1)
            found = True
            break
        elif M_num > N_list[mid]:
            left = mid + 1
            
        else:
            right = mid - 1
    if not found:
        print(0)
    
        