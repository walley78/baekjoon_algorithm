from itertools import combinations_with_replacement  # 중복 조합을 생성하기 위한 라이브러리
from heapq import heappush, heappop  # 우선순위 큐 구현을 위한 라이브러리


def calculate_wait_time(reqs, type_mentors, k):
    # mentors_available: 각 상담 유형별로 멘토들의 상담 종료 시간을 저장하는 우선순위 큐
    # key: 상담 유형 (1부터 k까지), value: 해당 유형 멘토들의 상담 종료 시간 리스트
    mentors_available = {i: [] for i in range(1, k + 1)}
    total_wait = 0  # 전체 대기 시간을 저장할 변수

    # 각 상담 요청에 대해 처리
    # start: 상담 요청 시각
    # duration: 상담 시간
    # type_id: 상담 유형
    for start, duration, type_id in reqs:
        queue = mentors_available[type_id]  # 현재 상담 유형의 멘토 큐 가져오기

        # 현재 시각(start)보다 일찍 끝난 상담들을 큐에서 제거
        while queue and queue[0] <= start:
            heappop(queue)

        # 상담 가능한 멘토가 있는 경우 (큐의 크기가 해당 유형의 멘토 수보다 작은 경우)
        if len(queue) < type_mentors[type_id - 1]:
            heappush(queue, start + duration)  # 새로운 상담 종료 시간을 큐에 추가
        else:
            # 모든 멘토가 상담 중인 경우
            next_available = heappop(queue)  # 가장 빨리 끝나는 상담 시간
            wait_time = max(0, next_available - start)  # 대기 시간 계산
            total_wait += wait_time  # 전체 대기 시간에 추가
            heappush(queue, next_available + duration)  # 새로운 상담 종료 시간을 큐에 추가

    return total_wait


def solution(k, n, reqs):
    # 상담 요청을 시작 시간 순으로 정렬
    reqs.sort(key=lambda x: x[0])

    # 최소 대기 시간을 저장할 변수를 무한대로 초기화
    min_wait_time = float('inf')

    # combinations_with_replacement를 사용하여 멘토 배분의 모든 가능한 조합 생성
    # range(k): 0부터 k-1까지의 숫자 (각 상담 유형을 나타냄)
    # n-k: 남은 멘토 수 (각 유형당 1명을 할당하고 남은 수)
    for comb in combinations_with_replacement(range(k), n - k):
        # 각 유형별로 최소 1명의 멘토 할당으로 시작
        mentors = [1] * k

        # 현재 조합에 따라 나머지 멘토들을 배분
        # type_idx: 추가 멘토를 배정할 상담 유형
        for type_idx in comb:
            mentors[type_idx] += 1

        # 현재 멘토 배분에 대한 대기 시간 계산
        wait_time = calculate_wait_time(reqs, mentors, k)
        # 최소 대기 시간 갱신
        min_wait_time = min(min_wait_time, wait_time)

    return min_wait_time