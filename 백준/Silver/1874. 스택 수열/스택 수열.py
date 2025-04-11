#1874 - 스택 수열 

#스택에 push 하는 순서는 반드시 오름차순을 지키도록 
# 
import sys
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
#[4, 3, 6, 8, 7, 5, 2, 1]
cnt = 1
stack = []
result = []
answer = True
for num in numbers:
    while cnt<=num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        answer = False
        break
if answer:
    for r in result:
        print(r)
else:
    print('NO')
