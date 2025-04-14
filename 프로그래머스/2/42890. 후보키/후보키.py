from itertools import combinations

def solution(relation):
    n_col = len(relation[0])
    n_row = len(relation)
    all_combis = []

    # 1. 모든 컬럼 조합을 만든다
    for r in range(1, n_col+1):
        for combi in combinations(range(n_col), r):
            # 2. 유일성 검사
            seen = set()
            for row in relation:
                key = tuple(row[i] for i in combi)
                seen.add(key)
            if len(seen) == n_row:
                all_combis.append(set(combi))

    # 3. 최소성 검사
    candidate_keys = []
    for c in sorted(all_combis, key=lambda x: len(x)):
        if all(not c.issuperset(ck) for ck in candidate_keys):
            candidate_keys.append(c)

    return len(candidate_keys)
