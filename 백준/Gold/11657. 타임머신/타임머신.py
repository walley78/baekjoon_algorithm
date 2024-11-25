import sys

input = sys.stdin.readline

def bellman_ford(N, M, edges):
    # 최단 거리를 저장하는 배열 초기화
    dist = [float('inf')] * (N + 1)
    dist[1] = 0  # 1번 도시에서 출발

    # N-1번 동안 모든 간선을 완화 (Relaxation)
    for i in range(N - 1):
        for A, B, C in edges:
            # 시작 도시(A)가 도달 가능하고, 현재 간선을 통해 더 짧은 경로를 발견한 경우
            if dist[A] != float('inf') and dist[A] + C < dist[B]:
                dist[B] = dist[A] + C

    # 음수 사이클 탐지
    for A, B, C in edges:
        # N-1번 완화 후에도 여전히 더 짧아질 수 있으면 음수 사이클 존재
        if dist[A] != float('inf') and dist[A] + C < dist[B]:
            return -1  # 음수 사이클 존재 시 -1 반환

    # 도달할 수 없는 도시는 -1로 처리
    return [dist[i] if dist[i] != float('inf') else -1 for i in range(2, N + 1)]


N, M = map(int, input().split())
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))  # 간선 정보를 저장


result = bellman_ford(N, M, edges)


if result == -1:
    print(-1)  # 음수 사이클이 있는 경우
else:
    print("\n".join(map(str, result)))  # 각 도시로 가는 최단 시간을 출력