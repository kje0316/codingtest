N = int(input())
num = []

for n in range(1, N):
    score = n + sum(map(int, str(n)))
    if score == N:
        num.append(n)
if len(num) == 0:
    print(0)
else:
    print(min(num))    
