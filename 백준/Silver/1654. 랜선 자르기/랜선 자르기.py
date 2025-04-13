import sys

K, N = map(int, input().split()) #가지고 있는 랜선 수. 필요한 랜선 개수

k_list = [int(sys.stdin.readline()) for _ in range(K)]

start = 1
end = max(k_list) #제일 긴 길이 
result =  0 
while start <= end:
    mid = (start + end)//2 #길이 
    count = 0
    for k in k_list:
        count += k//mid #조각 수 
    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
    
    
print(result)
