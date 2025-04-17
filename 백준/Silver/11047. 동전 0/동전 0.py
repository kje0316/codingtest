#그리디 알고리즘 

#N 동전의 개수 
#K 합

import sys
N, K = map(int, input().split()) 
 
coin = [int(sys.stdin.readline().strip()) for _ in range(N)]
coin.sort(reverse=True) #큰 동전부터 
cnt = 0
for c in coin:
    if K>=c: #
        cnt += K//c
        K = K%c
print(cnt)
        
# print(coin)