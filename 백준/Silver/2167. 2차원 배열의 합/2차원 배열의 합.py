# N, M = map(int, input().split())
# #2차원 배열 
# arr = []
# for _ in range(N): #N*M 배열
#     t = list(map(int, input().split()))
#     arr.append(t)
# # print(arr)
# K = int(input())
# for _ in range(K): #4개의 정수 입력 
#     sum = 0
#     i, j, x, y = map(int, input().split()) #[1][1]~[2][3]
#     if i == x:
#         for a in range(j, y+1): #1 2 / 1 2
#             sum += arr[i-1][a-1] 
#         print(sum)
#     else: #1, 1 ~ 2, 3 => [1][1] [1][2]
#         for a in range(i-1, x):
#             for b in range(j-1, y):
#                 sum+= arr[a-1][b-1]
#         print(sum)
        
#     #(1,3) ~ (2, 3) => 
         
# import sys        
            
# N, M = map(int, input().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# K = int(input())
# for _ in range(K):
#     sum_val = 0
#     i, j, x, y = map(int, input().split())
#     for a in range(i-1, x):
#         for b in range(j-1, y):
#             sum_val += arr[a][b]
#     print(sum_val)
# 시간초과

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 누적합 배열 생성 (1-indexed로 padding)
psum = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        psum[i][j] = arr[i-1][j-1] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1]


K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = psum[x][y] - psum[i-1][y] - psum[x][j-1] + psum[i-1][j-1]
    print(result)