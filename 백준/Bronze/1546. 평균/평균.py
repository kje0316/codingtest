N =int(input()) #시험 과목 개수 
score = list(map(int, input().split())) #점수
print(sum(score)/max(score)*100/N)
