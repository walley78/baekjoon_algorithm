import sys
from collections import deque
from copy import deepcopy
from heapq import heappop, heappush

input = sys.stdin.readline

# 상 하 좌 우
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dijkstra(r, c):
    global mincount
    hq = [(rupees[r][c], r, c)]
    # visited = set()
    # visited = [[False]*N for _ in range(N)]
    # visited[r][c] = True
    visited = [[float('inf')]*N for _ in range(N)]
    while hq:
        count, cr, cc = heappop(hq)
        if (cr, cc) == (N-1, N-1):
            if count < mincount:
                mincount = count
            return
        for d in range(4):
            nr, nc = cr+dir[d][0], cc+dir[d][1]
            if 0 <= nr < N and 0 <= nc < N:
                # if (cr, cc, nr, nc) not in visited:
                if count+rupees[nr][nc] < visited[nr][nc]:
                    # visited.add((cr, cc, nr, nc))
                    visited[nr][nc] = count+rupees[nr][nc]
                    heappush(hq, (count + rupees[nr][nc], nr, nc))
    return

flag = True
count = 0
while flag:
    N = int(input())
    mincount = float('inf')
    if N == 0:
        flag = False
        break
    count += 1
    rupees = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[False]*N for _ in range(N)]
    # visited[0][0] = True
    visited = [[999999999999]*N for _ in range(N)]
    # dfs(0, 0, rupees[0][0])
    dijkstra(0, 0)
    print(f"Problem {count}: {mincount}")