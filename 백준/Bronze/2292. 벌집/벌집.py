N = int(input())
n = 1
score = 1
while True:
    score += (n-1)*6
    if N <= score:
        print(n)
        break
    n += 1
