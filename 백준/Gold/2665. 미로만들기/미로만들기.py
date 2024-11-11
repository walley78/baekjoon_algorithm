import sys
import heapq

input = sys.stdin.readline

def bfs(N, maze):
    # Priority queue for processing, stored as tuples (cost, row, column)
    heap = []
    heapq.heappush(heap, (0, 0, 0))  # (transformation count, start row, start column)

    # Track the minimum cost to reach each cell
    min_cost = [[float('inf')] * N for _ in range(N)]
    min_cost[0][0] = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while heap:
        cost, r, c = heapq.heappop(heap)

        # If we reached the bottom-right corner
        if r == N - 1 and c == N - 1:
            return cost

        # Check all 4 potential directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                # Calculate new cost if this is a black room
                new_cost = cost + (1 if maze[nr][nc] == 0 else 0)
                # Only consider this new path if it's cheaper
                if new_cost < min_cost[nr][nc]:
                    min_cost[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))

    return float('inf')  # If no path is found, though theoretically impossible with given problem constraints



# 한 줄에 들어가는 방의 수
N = int(input())

# 0은 검은방, 1은 흰 방
maze = [list(map(int, input().strip())) for _ in range(N)]

result = bfs(N, maze)
print(result if result != float('inf') else 0)