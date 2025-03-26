text = [input() for _ in range(3)] #fizz buzz 11
n = 0
index = 0
for t in range(len(text)): 
    if 'Fizz' in text[t] or 'Buzz' in text[t]:
        n += 1
    else:
        num = int(text[t])
        num += (3-t)
        break
    
if n == 3:
    print("Fizz")
else:
    if num%3==0 and num%5 ==0 :
        print('FizzBuzz')
    elif num%3==0 and num%5!=0:
        print('Fizz')
    elif num%3!=0 and num%5==0:
        print('Buzz')
    else:
        print(num)
     