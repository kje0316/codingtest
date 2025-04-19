import sys
N, M = map(int, input().split())


pw_dict = {}
for _ in range(N):
    text = sys.stdin.readline().strip()
    ad, pw = text.split()
    pw_dict[ad] =  pw
    
for _ in range(M):
    t = sys.stdin.readline().strip()
    # print(t)
    print(pw_dict[t])