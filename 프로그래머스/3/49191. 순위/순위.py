def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]

    # 이김 표시
    for a, b in results:
        graph[a][b] = 1   # a가 b를 이김
        graph[b][a] = -1  # b는 a에게 짐

    # 플로이드 워셜: i가 k를 알고 있고, k가 j를 안다면 i는 j도 안다
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1

    # 각 선수마다 확실한 관계가 n - 1개 있으면 순위가 확정됨
    answer = 0
    for i in range(1, n+1):
        known = 0
        for j in range(1, n+1):
            if graph[i][j] != 0:
                known += 1
        if known == n - 1:
            answer += 1

    return answer
