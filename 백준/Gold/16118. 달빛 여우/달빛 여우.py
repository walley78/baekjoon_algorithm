import heapq
import sys
input = sys.stdin.read
INF = int(1e18)

def dijkstra_fox(start, graph, N):
    dist = [INF] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, now = heapq.heappop(heap)
        if dist[now] < cost:
            continue
        for next, w in graph[now]:
            new_cost = cost + w
            if dist[next] > new_cost:
                dist[next] = new_cost
                heapq.heappush(heap, (new_cost, next))
    return dist

def dijkstra_wolf(start, graph, N):
    dist = [[INF] * 2 for _ in range(N + 1)]
    dist[start][0] = 0  # 0: 다음 이동은 달리기(2배 속도)
    heap = [(0, start, 0)]  # (시간, 노드, 상태)
    while heap:
        cost, now, state = heapq.heappop(heap)
        if dist[now][state] < cost:
            continue
        for next, w in graph[now]:
            if state == 0:
                new_cost = cost + w // 2  # 달릴 차례면 2배 빠름
                if dist[next][1] > new_cost:
                    dist[next][1] = new_cost
                    heapq.heappush(heap, (new_cost, next, 1))
            else:
                new_cost = cost + w * 2  # 걸을 차례면 0.5배 속도
                if dist[next][0] > new_cost:
                    dist[next][0] = new_cost
                    heapq.heappush(heap, (new_cost, next, 0))
    return dist

def solve():
    data = input().split()
    idx = 0
    N, M = int(data[idx]), int(data[idx+1])
    idx += 2
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, d = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        graph[a].append((b, d * 2))  # 여우 거리 단위 = 2배
        graph[b].append((a, d * 2))

    fox_dist = dijkstra_fox(1, graph, N)
    wolf_dist = dijkstra_wolf(1, graph, N)

    count = 0
    for i in range(2, N + 1):  # 1번은 시작점이므로 제외
        if fox_dist[i] < min(wolf_dist[i][0], wolf_dist[i][1]):
            count += 1
    print(count)

solve()
