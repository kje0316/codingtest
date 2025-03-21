N = input()

dic = {'A':4.0,'B':3.0, 'C':2.0,'D':1.0,'F':0.0}
if N =='F':
    print(0.0)
else:
    if N[-1]=='+':
        print(dic[N[0]]+0.3)
    elif N[-1] == '-':
        print(dic[N[0]]-0.3)
    else:
        print(dic[N[0]])