#낮에 A미터 올라가기. 밤에 B 미끄러지기/ V 높이
import math
A, B, V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))