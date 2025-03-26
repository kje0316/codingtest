import math
N = int(input())
num = str(math.factorial(N))
count = 0
for i in num[::-1] :
    if int(i) != 0:
        print(count)
        break
    count += 1
