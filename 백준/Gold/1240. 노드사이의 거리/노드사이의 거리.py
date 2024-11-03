import sys
from collections import deque

input = sys.stdin.read

def finddistance(start, end):
    if start == end:
        return 0
    
    queue = deque([(start, 0)])  # Queue holds tuples of (current_node, cumulative_distance)
    visited = [False] * (N + 1)
    visited[start] = True
    
    while queue:
        current, current_dist = queue.popleft()
        for neighbor, dist in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                total_dist = current_dist + dist
                if neighbor == end:
                    return total_dist
                queue.append((neighbor, total_dist))
    
    return -1  # Return -1 if no path is found

# Reading input
data = input().split()
N = int(data[0])
M = int(data[1])

graph = [[] for _ in range(N+1)]
index = 2

for _ in range(N-1):
    node1 = int(data[index])
    node2 = int(data[index + 1])
    distance = int(data[index + 2])
    graph[node1].append((node2, distance))
    graph[node2].append((node1, distance))
    index += 3

results = []
for _ in range(M):
    s1 = int(data[index])
    s2 = int(data[index + 1])
    index += 2
    results.append(finddistance(s1, s2))

for result in results:
    print(result)
