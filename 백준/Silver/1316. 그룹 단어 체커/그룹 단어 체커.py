N = int(input())
answer = N
for _ in range(N):
    t_list = []
    text = input()
    for t in text:
        if t not in t_list:
            t_list.append(t)
    index = []
    for char in t_list:
        for i in range(len(text)):
            if text[i] == char:
                index.append(i)
    
    for i in range(1, len(index)):
        if index[i] != index[i-1] + 1 :
            answer -= 1
            break
print(answer)