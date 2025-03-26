N, K = map(int, input().split())

# import math
# print(int(math.factorial(N)/math.factorial(K)/math.factorial(N-K)))
n = 1
for i in range(N, N-K, -1):
    n *= i
k = 1
for j in range(1,K+1):
    k *= j
print(int(n/k))