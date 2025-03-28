N = int(input())

for i in range(1,N+1): # 1 2 3 4 
    if i ==1:
        print(' '*(N-i)+'*'*i)
    elif i == N:
        print('*'*(2*i-1))
    elif i > 1: #2
        print(' '*(N-i)+'*'+' '*(2*i-3)+'*')