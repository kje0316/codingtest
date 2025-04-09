import sys
N, M  = map(int, input().split())
poket = [sys.stdin.readline().strip() for _ in range(N)]
poket_dict = {p:i+1 for i,p in enumerate(poket)}

# for _ in range(M): 
#     text = input()
#     try:
#         int(text)
#         answer = True
#     except ValueError:
#         answer = False
        
#     if answer:
#         print(poket[int(text)-1])
#     else:
#         print(poket.index(text)+1)
    
for _ in range(M):
    text = input()
    try :
        int(text)
        answer = True
    except ValueError:
        answer = False
    
    if answer : #
        print(poket[int(text)-1])
    else:
        print(poket_dict[text])