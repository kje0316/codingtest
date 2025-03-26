N, M = map(int, input().split())
num = []
for i in range(1,N+1): 
    if M%i==0 and N%i==0:
        num.append(i)
print(max(num)) #최소 공배수

score = N # 24 18
while True:
    if score%N==0 and score%M==0:
        print(score)
        break
    score += N
    