#a층 b호 -> 
import sys
 #케이스의 수 
#answer = 0
# def c_people(k, n):
#     cnt = 0
#     for i in range(k):
#         for j in range(1, n+1):
#             cnt += j
#     return cnt + c_people(k-1, n)
#0층 1 ... n => 
#1층 3호 -> 0층 1호 2호 3호
#2층 3호 -> 1층 1호 2호 3호 

#재귀 사용  -> 시간 초과  
# def c_people(k, n):
#     if k == 0:
#         return n
#     if n == 1:
#         return 1
#     return c_people(k, n-1) + c_people(k-1, n)

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     print(c_people(k,n))
# T= int(input())
# for _ in range(T):
#     k= int(input())
#     n = int(input())
    
#     numbers = [0,0]#이걸로 층마다 저장할 이중 리스트 만들고 
#     for i in range(k):
#         for j in range(1, n+1):
#             numbers[i][j] = 

# numbers = [0]* 
#1층 3호 -> 0층 1호, 2호, 3호 => 1+2+3 = 6
#2층 3호 -> 1층 1호,2호,3호
#       -> 0층 1호/0층 1호 2호/0층 1호2호3호
#number[i][j] = number[i][j-1]+number[i-1][j]
#0층 n호 ->n 명
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    number = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1, n+1):
        number[0][i] = i
    for i in range(1,k+1):
        for j in range(n+1):
            number[i][j] = number[i][j-1] + number[i-1][j]
    print(number[k][n])


#1 3 6 10
#1 2 3 4 5 
