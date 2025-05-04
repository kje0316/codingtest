#1057- 토너먼트
#N명의 참가자 
round = 0
N, A, B = map(int, input().split())
while A != B:
    A = (A+1)//2
    B = (B+1)//2
    round +=1
print(round)