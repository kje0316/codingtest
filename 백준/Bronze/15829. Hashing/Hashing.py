#입력 문자열은 소문자 
import string
L = int(input()) #문자열의 길이 
text = input() #영문 소문자
M = 1234567891 #소수
alpha = [i for i in string.ascii_lowercase]
score = 0
for i in range(L): # 0, 1, 2
    index = alpha.index(text[i]) #z
    score += (index+1)*(31**i)
score = score %M
print(score)