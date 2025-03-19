    

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    a = A%10
    if a in [1, 5, 6]:
        print(a)
    elif a == 0 :
        print(10)
    elif a in [4, 9]:
        if B%2==1:
            print(a)
        else :
            print(a**2%10)
    else:
        print(a**B%10)