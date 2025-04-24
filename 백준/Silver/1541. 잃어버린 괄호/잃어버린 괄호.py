import sys 

text = sys.stdin.readline()

#최소화 -> -를 기준으로 묶기 
parts = text.split('-')
result = []
for p in parts:
    sum = 0
    if '+' in p: #
        plus = p.split('+')
        for i in plus:
            sum += int(i)
        result.append(sum)
    else:
        sum = int(p)
        result.append(sum)

# print(result)

if len(result) == 1:
    print(result[0])
else:
    answer = result[0]
    for r in range(1, len(result)):
        answer -= result[r]

    print(answer)