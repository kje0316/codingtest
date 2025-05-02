x, y = input().split()
result = []
m =0
while m+len(x)<=len(y):
    cnt = 0
    Y = y[m:]
    for i in range(len(x)):
        if x[i] != Y[i]:
            cnt += 1
    m += 1
    result.append(cnt)

print(min(result))