def solution(n):
    answer = 0
    a = n**(1/2)
    if n%a == 0:
        answer = (a+1)**2
    else:
        answer = -1
    return answer