N = int(input())
for _ in range(N):
    text = input()
    score = 0
    streak = 0 #연속된 O의 수
    for t in text:
        if t == 'O':
            streak += 1 #OOXXOXXOOO
            score += streak
        else :
            streak = 0
    print(score)       
