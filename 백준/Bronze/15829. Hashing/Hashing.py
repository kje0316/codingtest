#입력 문자열은 소문자 
import string
L = int(input()) #문자열의 길이 
text = input() #영문 소문자
alpha = [i for i in string.ascii_lowercase]
num = list(range(1,27))
alpha_dict = {i:n for i, n in zip(alpha,num)}
hash = []
for t in text:
    hash.append(alpha_dict[t]) #입력된 문자열의 숫자 입력
score = 0
for i, j in enumerate(hash): #[2, 5, 8]이라면 0, 2/2,5
    score += (j * 31**i)
print(score)