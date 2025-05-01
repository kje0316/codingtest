n = int(input())
#한수 : 각 자리가 등차수열을 이루는 수
def is_hansu(n):
    digits = list(map(int, str(n)))
    if len(digits) <= 2:
        return True
    diff = digits[1] - digits[0]
    for i in range(1, len(digits)-1):
        if digits[i+1] - digits[i] != diff:
            return False
    return True
cnt = 0
for i in range(1, n+1):
    if is_hansu(i):
       cnt +=1
print(cnt) 