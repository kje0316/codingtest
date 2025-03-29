from collections import deque

N = int(input())
num_list = deque(range(1,N+1))

count = 1
while len(num_list) >1:
    if count%2==1:
        num_list.popleft()
    elif count%2==0:
        num_list.append(num_list.popleft())
    count+=1
print(num_list[0])
