# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

import sys
from collections import deque
input = sys.stdin.readline

# 지도의 크기
N = int(input())
housemap = [list(map(int, input().strip())) for _ in range(N)]

# 0으로 감싸
housemap.insert(0, [0]*N)
housemap.append([0]*N)
for arr in housemap:
    arr.insert(0, 0)
    arr.append(0)

# print(map)

# 상  하  좌  우
# -1  1  0  0
# 0   0  -1 1
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

house_num = []

def bfs(sr, sc):
    queue = deque([(sr, sc)])
    housemap[sr][sc] = 0
    count = 1

    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr, nc = cr + dir[d][0], cc + dir[d][1]
            if housemap[nr][nc] == 1:
                count += 1
                housemap[nr][nc] = 0
                queue.append((nr, nc))

    house_num.append(count)

cluster = 0
for r in range(1, N+1):
    for c in range(1, N+1):
        if housemap[r][c] == 1:
            cluster += 1
            bfs(r, c)

print(cluster)
house_num.sort()
for num in house_num:
    print(num)

