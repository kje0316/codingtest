N = int(input())
order_list = [input() for _ in range(N)]
num_list = []
for order in order_list:
    if 'push' in order:
        num_list.append(order.split(" ")[-1])
    elif 'pop' in order:
        if len(num_list) >= 1:
            pop_num = num_list.pop()
            print(pop_num)
        else:
            print(-1)
            
    elif 'size' in order:
        print(len(num_list))
    
    elif 'empty' in order:
        if len(num_list) == 0:
            print(1)
        else:
            print(0)
    
    else:
        if len(num_list) == 0:
            print(-1)
        else:
            print(num_list[-1])