#1358 - 하키 

W, H, X, Y, P = map(int,input().split()) #p 선수의 수 1
cnt = 0
for _ in range(P):
    x, y = map(int, input().split()) #좌표 
    if X <= x <= X+W and Y <= y <= Y+H:
        cnt += 1
    elif (x-X)**2 + (y - (Y+H/2))**2 <= (H/2)**2:
        cnt +=1 
    elif (x-(X+W))**2 + (y - (Y +H/2))**2 <= (H/2)**2:
        cnt +=1
print(cnt)