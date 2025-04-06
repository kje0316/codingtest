
X = int(input())

N = 64
N_list = [64,32,16,8,4,2,1]

    
count = 0 #[64, 32, 16, 8, 4, 2, 1]
for n in N_list: # 23
    if X >= n:
        count +=1
        X -= n
print(count)
