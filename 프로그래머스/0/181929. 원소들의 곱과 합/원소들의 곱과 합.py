def solution(num_list):
    sum = 0
    p = 1
    for num in num_list:
        sum += num
        p *= num
    if p < sum**2:
        return 1
    else:
        return 0