N, M = map(int, input().split())

result = [True]*(M+1)
result[0] = result[1] = False #

for i in range(2, int(M**0.5)+1):
    if result[i]:
        for j in range(i*i, M+1,i):
            result[j]= False

for i in range(N, M+1):
    if result[i]:
        print(i)

        