import sys

S = set()
M = int(input())
for _ in range(M):
    text = sys.stdin.readline().strip()  
    if text == 'all':
        S = set(range(1, 21))
    elif text == 'empty':
        S = set()
    else:
        t, *rest = text.split()
        x = int(rest[0])

        if t == 'add':
            S.add(x)
        elif t == 'remove':
            S.discard(x)
        elif t == 'check':
            print(1 if x in S else 0)
        elif t == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)