#체스판 다시 칠하기 
import sys
N, M = map(int, sys.stdin.readline().split())
Text = [sys.stdin.readline().rstrip() for _ in range(N)]
# print(Text)
chess1 = ['WBWBWBWB','BWBWBWBW']*4
chess2 = ['BWBWBWBW','WBWBWBWB']*4
# print(chess1)
# text[0][0:8]/ text[0][1:9]/text[0][2:10]~text[0][15:23]
# text[7][0:8]/ text[0][1:9]/text[0][2:10]~text[0][15:23]
# text[1][0:8]/ text[1][1:9]/text[1][2:10]~text[1][15:23]
# text[8][0:8]/ text[0][1:9]/text[0][2:10]~text[0][15:23]
count_list = []
for n in range(M-7): #0 1
    for m in range(N-7): #0 1 ~15
        count1 = 0
        count2 = 0
        for i in range(8):
            for j in range(8):
                if Text[m + i][n + j] != chess1[i][j]:
                    count1 += 1
                if Text[m + i][n + j] != chess2[i][j]:
                    count2 += 1
        count_list.append(count1)
        count_list.append(count2)
print(min(count_list))