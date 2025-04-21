import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visited = [False] * N
groups = []

# 친구 그룹 찾기 (BFS)
def bfs(start):
    q = deque([start])
    visited[start] = True
    count = 1
    total = candies[start]
    while q:
        curr = q.popleft()
        for nxt in adj[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1
                total += candies[nxt]
    return (count, total)

# 모든 친구 그룹 구성
for i in range(N):
    if not visited[i]:
        groups.append(bfs(i))

# 0-1 Knapsack: 그룹 인원 수 = 무게, 사탕 수 = 가치
dp = [0] * K
for weight, value in groups:
    for j in range(K - 1, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K - 1])
