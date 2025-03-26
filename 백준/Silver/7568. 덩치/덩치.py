N = int(input())

num = [list(map(int, input().split())) for _ in range(N)]
for i in num: 
    count = 0
    for j in num:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    print(count+1, end=" ")
