N = int(input())
order_list = [input() for _ in range(N)]
num_list = []
for order in order_list:
    if 'push' in order:
        num = order.split()[-1]
        num_list.append(num)
    elif 'pop' in order:
        if len(num_list) == 0:
            print(-1)
        else:
            num = num_list.pop(0)
            print(num)
    elif 'size' in order:
        print(len(num_list))
    elif 'empty' in order:
        if len(num_list) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in order:
        if len(num_list) == 0:
            print(-1)
        else:
            print(num_list[0])
    else:
        if len(num_list)==0:
            print(-1)
        else:
            print(num_list[-1])
        
            