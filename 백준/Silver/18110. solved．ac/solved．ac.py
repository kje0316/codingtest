import math
import sys
n = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

m = math.floor(n*0.15+0.5) #제외하는 
numbers = sorted(numbers)
 
if n==0:
    print(0) 
elif n>2*m:
    numbers = numbers[m:n-m]
    print(math.floor(sum(numbers)/len(numbers)+0.5))    

else:
    print(0)