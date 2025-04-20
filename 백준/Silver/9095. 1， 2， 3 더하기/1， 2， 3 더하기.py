#알고리즘 - 다이나믹 프로그래밍(DP)

n = int(input())

number = [int(input()) for _ in range(n)]
max_num = max(number)
dp = [0] * (max_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_num+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for n in number:
    print(dp[n])