def solution(n):
    n = str(n)
    n = sorted(n)
    n= ''.join(n)[::-1]
    n = int(n)
    return n