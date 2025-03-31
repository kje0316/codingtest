K = int(input())
numbers = [int(input()) for _ in range(K)]
#10/ 1 3 5 4 0 0 7 0 0 6
new_num = []
for num in numbers:
    if num != 0:
        new_num.append(num)
    else:
        new_num.pop()
print(sum(new_num))