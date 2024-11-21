import sys
input = sys.stdin.readline
from collections import deque
import copy

# NXM 배열
N, M = map(int, input().split())

mars = [list(map(int, input().split())) for _ in range(N)]

dp = [[-999999999999999]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 왼쪽, 오른쪽, 아래
dir = [[0, -1], [0, 1], [1, 0]]


startcount = mars[0][0]
stack = deque([(1, 0)])
dp[0][0] = startcount

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + mars[0][j]
#     if N > 1:
#         dp[1][j] = dp[0][j] + mars[1][j]
#
# if N > 1:
#     dp[1][0] = dp[0][0] + mars[1][0]
#     dp[1][-1] = dp[0][-1] + mars[1][-1]

for i in range(1, N):
    listleft = [-99999999999999999999]*M
    listright = [-9999999999999999999]*M

    for j in range(M):
        if j == 0:
            listleft[j] = dp[i-1][0]+mars[i][0]
            listright[M-1] = dp[i-1][M-1]+mars[i][M-1]
            continue

        listleft[j] = mars[i][j] + max(dp[i-1][j], listleft[j-1])
        listright[M-1-j] = mars[i][M-1-j] + max(dp[i-1][M-1-j], listright[M-j])

    temp = [max(listleft[j], listright[j]) for j in range(M)]
    dp[i] = copy.deepcopy(temp)

print(dp[N-1][M-1])