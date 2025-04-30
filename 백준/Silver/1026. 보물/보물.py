n = int(input())

A = list(map(int, input().split()))  # 재배열 가능
B = list(map(int, input().split()))  # 재배열 불가능

A.sort()                  
B_sorted = sorted(B, reverse=True)  

result = 0
for i in range(n):
    result += A[i] * B_sorted[i]

print(result)