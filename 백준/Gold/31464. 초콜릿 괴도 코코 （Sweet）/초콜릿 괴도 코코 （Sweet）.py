import sys
from collections import deque

input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(r, c, N):
    return 0 <= r < N and 0 <= c < N

def count_components(grid, N):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '#' and not visited[r][c]:
                count += 1
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc
                        if in_bounds(nr, nc, N) and grid[nr][nc] == '#' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
    return count

def all_edges_are_bridges(grid, N):
    nodes = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '#':
                nodes.append((r, c))

    node_count = len(nodes)
    edge_set = set()
    for r, c in nodes:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, N) and grid[nr][nc] == '#':
                a, b = (r, c), (nr, nc)
                if a > b:
                    a, b = b, a
                edge_set.add((a, b))

    edge_count = len(edge_set)
    if edge_count != node_count - 1:
        return False

    visited = set()
    def dfs(r, c):
        visited.add((r, c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, N) and grid[nr][nc] == '#' and (nr, nc) not in visited:
                dfs(nr, nc)

    dfs(nodes[0][0], nodes[0][1])
    return len(visited) == node_count

# 입력 처리
N = int(input())
grid = []
for _ in range(N):
    line = input().strip()
    grid.append(list(line))

results = []

for r in range(N):
    for c in range(N):
        if grid[r][c] == '#':
            grid[r][c] = '.'
            if count_components(grid, N) == 1 and all_edges_are_bridges(grid, N):
                results.append((r + 1, c + 1))
            grid[r][c] = '#'

# 출력
print(len(results))
for r, c in sorted(results):
    print(r, c)