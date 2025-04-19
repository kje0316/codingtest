import sys
T = int(input())

#피보나치가 적혀있는 수를 
#출력을 2개 : 0이 출력되는 횟수 / 1이 출력되는 횟수 
fibo = [(0,0)]*41
fibo[0] = (1, 0)
fibo[1] = (0, 1)

for i in range(2, 41):
    fibo[i] = (fibo[i-1][0] + fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1])
for _ in range(T):
    num = int(sys.stdin.readline())
    print(*fibo[num])