X = int(input()) #영수증 금액
N = int(input()) #물건 종류
price = 0
while N >0:
    a, b = map(int, input().split())
    price += a*b
    N = N -1

if X == price:
    print("Yes") 
else:
    print("No")     