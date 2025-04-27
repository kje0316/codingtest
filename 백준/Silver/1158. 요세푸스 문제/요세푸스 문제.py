n, k = map(int, input().split())

num = list(range(1, n+1)) #
result = []
idx = 0

while num:
    idx = (idx+k-1)%len(num)
    result.append(num[idx])
    num.pop(idx)
    
print("<" + ", ".join(map(str, result)) + ">")