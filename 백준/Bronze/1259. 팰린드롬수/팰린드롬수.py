import sys
while True:
    n = input()
    if int(n) == 0:
        break
    if n == n[::-1]:
        print('yes')

    else:
        print('no')
   
