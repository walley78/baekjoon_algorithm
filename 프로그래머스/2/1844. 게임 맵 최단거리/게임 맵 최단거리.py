from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    # count = []
    min_count = 999999999999999999
    # 나는 언제나 0,0에서 시작
    # 가야하는 곳은 언제나 (n, m)임
    # 상 하 우 좌
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    # 빈자리 (1) 찾아서 상하좌우로 이동하면서 cnt +1
    # n, m 도착하면 count에 append
    # 막혀있어서 영원히 도착 못하면 -1 return
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    def bfs(maps):
        stack = deque([(0, 0, 1)])
        while stack:
            r, c, cnt = stack.popleft()
            if (r, c) == (N - 1, M - 1):
                # if min_count > cnt and cnt > 1:
                #     min_count = cnt
                return cnt
            for d in range(4):
                nr, nc = r+dir[d][0], c+dir[d][1]
                if 0 <= nr < N and 0 <= nc < M:
                    if maps[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr, nc, cnt+1))
        return -1

    ans = bfs(maps)
    return ans