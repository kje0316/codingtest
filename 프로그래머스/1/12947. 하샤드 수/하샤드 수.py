def solution(x):
    num = [int(i) for i in str(x)]
    a = sum(num)
    if x%a ==0:
        return True
    else:
        return False