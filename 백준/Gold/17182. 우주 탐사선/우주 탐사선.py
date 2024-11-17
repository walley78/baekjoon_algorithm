import sys
from heapq import heappush, heappop  # 우선순위 큐를 위한 heapq 모듈 임포트
input = sys.stdin.readline

# N: 행성의 개수, K: 시작 행성의 위치
N, K = map(int, input().split())

time = [list(map(int, input().split())) for _ in range(N)]

def solve_planet_exploration():
    # 우선순위 큐를 사용하여 최단 시간 경로를 찾음
    # pq의 각 원소는 (총 이동시간, 현재 행성, 방문한 행성들의 상태) 형태
    # (1 << K)는 시작 행성 K를 방문했다는 것을 비트마스크로 표현
    pq = [(0, K, 1 << K)]

    # seen 딕셔너리: (현재 행성, 방문 상태)를 키로 하고, 해당 상태까지의 최소 시간을 값으로 저장
    seen = {}

    # 우선순위 큐가 빌 때까지 반복
    while pq:
        # 현재까지의 총 이동시간, 현재 위치한 행성, 지금까지 방문한 행성들의 상태를 큐에서 꺼냄
        total_time, current, visited = heappop(pq)

        # 만약 현재 상태가 이미 더 적은 시간으로 방문된 적이 있다면 스킵
        if (current, visited) in seen and seen[(current, visited)] < total_time:
            continue

        # 모든 행성을 방문했다면 ((1 << N) - 1은 N개의 모든 비트가 1인 상태)
        # 현재까지의 총 이동시간을 반환
        if visited == (1 << N) - 1:
            return total_time

        # 다음으로 방문할 수 있는 모든 행성들에 대해 반복
        for next_planet in range(N):
            # 현재 행성에 머무르는 경우는 제외
            if next_planet != current:
                # 다음 행성을 방문했다고 표시한 새로운 방문 상태 계산
                # OR 연산(|)을 통해 비트마스크에 다음 행성 추가
                new_visited = visited | (1 << next_planet)

                # 현재 위치에서 다음 행성까지의 이동시간을 더함
                new_time = total_time + time[current][next_planet]

                # 이 새로운 상태가 처음 방문되거나, 기존보다 더 빠른 시간으로 도달 가능한 경우
                if ((next_planet, new_visited) not in seen or
                        new_time < seen[(next_planet, new_visited)]):
                    # seen 딕셔너리 업데이트
                    seen[(next_planet, new_visited)] = new_time
                    # 우선순위 큐에 새로운 상태 추가
                    heappush(pq, (new_time, next_planet, new_visited))

    # 문제의 제약조건상 여기까지 도달할 수 없지만,
    # 모든 행성을 방문할 수 없는 경우를 위한 반환값
    return float('inf')


# 결과 출력
print(solve_planet_exploration())