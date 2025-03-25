N = int(input())
nums = list(map(int, input().split()))
t = 0
for i in nums: #1 3 5 7
    n = []
    for j in range(1, i+1): #5
        if i % j ==0:
            n.append(j)
    if len(n)==2:
        t += 1
print(t)