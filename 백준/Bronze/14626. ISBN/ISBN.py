number = input()
sum = 0
n = 0
for i in range(len(number)-1):
    if number[i]=='*':
        n = i 
        continue
    elif i%2==0:
        sum += int(number[i])
    else:
        sum += 3*int(number[i])
sum += int(number[-1])        
        
for i in range(10):
    total = sum
    if n%2==0:
        total += i
    else:
        total += 3*i
    
    if total%10 ==0:
        print(i)
        break
    