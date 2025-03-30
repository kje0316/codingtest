T = int(input())
text = [input() for _ in range(T)]
for t in text:
    count = 0
    answer = True
    for i in range(len(t)):
        if '(' == t[i]:
            count += 1
        elif ')' == t[i]:
            count -= 1
        if count < 0 :
            answer  = False
            break
    if answer == True:
        if count ==0:
            print("YES")
        else:
            print("NO")
    else :
        print("NO")
                    