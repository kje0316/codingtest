import heapq
import sys
N = int(input())
result = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0: #배열에 x추가 
        heapq.heappush(result, -x)
    else: #배열이 비어있으면 0 출력. 
        if len(result) == 0:
            print(0)
        else: #가장 큰 값을 출력하고 배열에서 제거 
            print(-result[0])
            heapq.heappop(result)
            
            

    