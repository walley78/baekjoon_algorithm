import sys
import heapq


def solve_min_cow_cost():
    N, M = map(int, sys.stdin.readline().split())

    # 인접 리스트 생성
    graph = [[] for _ in range(N + 1)]

    # 그래프
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 최소 거리 저장
    distances = [float('inf')] * (N + 1)
    distances[1] = 0

    # 우선순위 큐: (총 소 비용, 현재 노드, 현재까지의 최대 소 수)
    pq = [(0, 1)]

    while pq:
        total_cow_cost, current_node = heapq.heappop(pq)

        # 목적지에 도착했다면 총 소 비용 반환
        if current_node == N:
            return total_cow_cost

        # 이미 더 나은 경로를 찾았다면 건너뛰기
        if total_cow_cost > distances[current_node]:
            continue

        # 인접한 노드 탐색
        for next_node, cow_count in graph[current_node]:
            # 이 경로의 총 소 비용 계산
            new_total_cow_cost = total_cow_cost + cow_count

            # 더 나은 경로를 찾았다면
            if new_total_cow_cost < distances[next_node]:
                distances[next_node] = new_total_cow_cost
                heapq.heappush(pq, (new_total_cow_cost, next_node))


print(solve_min_cow_cost())