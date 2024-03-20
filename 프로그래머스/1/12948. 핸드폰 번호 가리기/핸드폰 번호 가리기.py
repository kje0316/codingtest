def solution(phone_number):
    answer = ''
    phone_number = list(phone_number)
    num = len(phone_number)
    for i in range(0,num-4):
        phone_number[i] = '*'
    answer = "".join(phone_number)
    return answer