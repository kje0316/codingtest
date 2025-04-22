n = int(input())

#2xn 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수
dp = [0]* (n+2)

dp[1] = 1
dp[2] = 3
if n > 2:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[n]%10007)