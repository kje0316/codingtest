import sys 
def cal(A, B):
    return((A+B)*(A-B))

A, B =  map(int, sys.stdin.readline().split())

print(cal(A,B))
