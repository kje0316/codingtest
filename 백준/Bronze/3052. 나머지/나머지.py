import sys
numbers = [int(sys.stdin.readline()) for _ in range(10)]
re = []
for i in numbers:
    re.append(i%42)
print(len(set(re)))