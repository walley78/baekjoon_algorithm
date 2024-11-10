def solve_maze(N, M, directions, costs):
    # Helper to get the next cell based on direction
    def next_cell(i, j):
        if directions[i][j] == 'U':
            return i - 1, j
        elif directions[i][j] == 'D':
            return i + 1, j
        elif directions[i][j] == 'L':
            return i, j - 1
        elif directions[i][j] == 'R':
            return i, j + 1

    # Check if the cell is within bounds
    def in_bounds(x, y):
        return 0 <= x < N and 0 <= y < M

    visited = [[False] * M for _ in range(N)]
    in_cycle = [[False] * M for _ in range(N)]
    trampoline_cost = 0
    stack = []

    # Iterative DFS to detect cycles and paths that exit the maze
    for start_i in range(N):
        for start_j in range(M):
            if visited[start_i][start_j]:
                continue

            stack.append((start_i, start_j))
            path = []  # To track the path for cycle detection
            path_indices = {}

            while stack:
                ci, cj = stack[-1]
                if visited[ci][cj]:
                    stack.pop()
                    if (ci, cj) in path_indices:
                        path.pop()
                        del path_indices[(ci, cj)]
                    continue

                visited[ci][cj] = True
                path.append((ci, cj))
                path_indices[(ci, cj)] = len(path) - 1

                ni, nj = next_cell(ci, cj)

                if not in_bounds(ni, nj):
                    # Escape from maze without a trampoline
                    while stack:
                        stack.pop()
                    break

                if (ni, nj) in path_indices:  # Cycle detected
                    cycle_start = path_indices[(ni, nj)]
                    cycle = path[cycle_start:]
                    if any(not in_cycle[x][y] for x, y in cycle):
                        min_cost = min(costs[x][y] for x, y in cycle)
                        trampoline_cost += min_cost
                        for x, y in cycle:
                            in_cycle[x][y] = True
                    while stack and stack[-1] != (ni, nj):
                        last = stack.pop()
                        if last in path_indices:
                            del path_indices[last]
                            path.pop()
                    continue

                if visited[ni][nj]:
                    continue

                stack.append((ni, nj))

    return trampoline_cost

# Input processing
N, M = map(int, input().split())
directions = [input().strip() for _ in range(N)]
costs = [list(map(int, input().split())) for _ in range(N)]

# Get result
result = solve_maze(N, M, directions, costs)
print(result)