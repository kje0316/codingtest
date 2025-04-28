import sys 
import heapq
N = int(input())

numbers = [int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(numbers) #힙정렬
for _ in range(len(numbers)):
    print(heapq.heappop(numbers))