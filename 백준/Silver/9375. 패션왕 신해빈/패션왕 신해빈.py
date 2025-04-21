from collections import defaultdict

n = int(input()) 

for _ in range(n):
    m = int(input())
    type_count = {}  
    clothes = [input().split() for _ in range(m)]
    for name, category in clothes:
        if category in type_count:
            type_count[category] += 1
        else:
            type_count[category] = 1

    answer = 1
    for count in type_count.values():
        answer *= (count + 1)  # 입지 않는 경우 포함

    print(answer - 1)  # 전부 안 입는 경우 제외