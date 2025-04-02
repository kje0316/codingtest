N=int(input())

text_list = [input() for _ in range(N)]

str_list = []
for i in range(len(text_list[0])): 
    count = 0
    for j in range(N-1): 
        if text_list[j][i] == text_list[j+1][i]:
            count +=1
    if count == N-1:
        str_list.append(text_list[0][i])
    else:
        str_list.append('?')
for t in str_list:
    print(t, end="")