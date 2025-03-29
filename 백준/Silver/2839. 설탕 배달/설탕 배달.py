N = int(input())

num = []
for i in range(N//3+1): 
    for j in range(N//5+1): 
        if 3*i + 5*j ==N:
            num.append(i+j)
if len(num) == 0:
    print(-1)
else:
    print(min(num))