N, Q = map(int, input().split())

N_list = [int(input()) for _ in range(N)]
acc =[]
time=0
for n in N_list:
    time += n
    acc.append(time)
#2 1 3 / => 2, 3, 6, ..
for _ in range(Q):
    t = int(input())
    for i, a in enumerate(acc):
        if t < a:
            print(i + 1)
            break
