from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    
    queue = deque([(i, p) for i, p in enumerate(n_list)])  # (문서번호, 중요도)
    cnt = 0

    while queue:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):  # 뒤에 더 중요한 문서가 있음
            queue.append(cur)
        else:  # 현재 문서 출력
            cnt += 1
            if cur[0] == M:
                print(cnt)
                break