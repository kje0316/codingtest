def solution(arr):
    answer = sorted(arr)
    num = answer[0]
    arr.remove(num)
    if arr:
        return arr
    else:
        return [-1]