import sys
from collections import Counter
N= int(input())
#산술평균
#중앙값
#최빈값
#범위 
number = [int(sys.stdin.readline()) for _ in range(N)]
number.sort()
#산술평균
print(round(sum(number)/N))
#중앙값
print(number[N//2])

#최빈값
counter = Counter(number)
# print(counter)
freq = counter.most_common(2)
if len(freq) > 1 and freq[0][1] == freq[1][1]:
    print(freq[1][0])  # 두 번째로 작은 값 출력
else:
    print(freq[0][0])  # 최빈값 출력
# 최빈값이 여러 개일 때 두 번째로 작은 값을 출력

print(number[-1]-number[0])