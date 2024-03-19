def solution(num):
    s = 0
    while s<500:
        if num ==1 :
            return s
        if num%2 == 0 :
            num = num/2
        else:
            num = num*3 +1
        s+=1
    return -1
    
