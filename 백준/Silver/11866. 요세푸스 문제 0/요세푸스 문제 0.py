N, K = map(int, input().split())
numbers = list(range(1,N+1))
new_num = []
count = 0
for _ in range(N): 
    count = (count+K-1)%len(numbers)
    new_num.append(numbers.pop(count))
print('<', end="")
for num in new_num:
    if num != new_num[-1]:
        print(num, end=", ")
    else:
        print(num,end="")
print('>')