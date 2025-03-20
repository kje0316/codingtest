#입력은 28개 출력은 2개
li = list(range(1,31)) 
for _ in range(28):
    N = int(input())
    li.remove(N)
print(li[0])
print(li[1])