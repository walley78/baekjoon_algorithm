from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    db = defaultdict(list)

    # 1. info 전처리: 모든 조건 조합에 대해 점수 저장
    for i in info:
        data = i.split()
        conditions = data[:-1]
        score = int(data[-1])

        for k in range(5):  # 0~4개 조건에 대해 '-' 대체
            for comb in combinations([0,1,2,3], k):
                temp = conditions[:]
                for idx in comb:
                    temp[idx] = '-'
                key = ' '.join(temp)
                db[key].append(score)

    # 2. 각 key에 해당하는 점수 리스트 정렬 (이진 탐색 가능하게)
    for key in db:
        db[key].sort()

    # 3. query 처리
    answer = []
    for q in query:
        q = q.replace(" and", "")  # and 제거
        q_parts = q.split()
        q_key = ' '.join(q_parts[:-1])
        q_score = int(q_parts[-1])

        if q_key in db:
            scores = db[q_key]
            idx = bisect_left(scores, q_score)  # 이진 탐색
            count = len(scores) - idx
            answer.append(count)
        else:
            answer.append(0)

    return answer
