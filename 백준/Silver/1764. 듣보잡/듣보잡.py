import sys
N, M = map(int, input().split()) #듣도못한 사람의수 N, 보도 못한 사람의 수 M

name1 = set(input() for _ in range(N))
name2 = set(input() for _ in range(M))

result = list(name1 & name2) #교집합
print(len(result))
result = sorted(result)
for i in result:
    print(i)
