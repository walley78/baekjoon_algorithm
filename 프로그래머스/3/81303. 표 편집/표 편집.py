def solution(n, k, cmd):
    # 각 인덱스의 이전, 다음 노드를 저장
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    next[n - 1] = -1  # 마지막 원소는 다음이 없음

    removed = []  # 삭제된 인덱스를 저장할 스택
    curr = k  # 현재 선택된 행 인덱스

    for command in cmd:
        if command[0] == 'U':  # 위로 이동
            x = int(command[2:])
            for _ in range(x):
                curr = prev[curr]
        elif command[0] == 'D':  # 아래로 이동
            x = int(command[2:])
            for _ in range(x):
                curr = next[curr]
        elif command[0] == 'C':  # 삭제
            removed.append(curr)
            if prev[curr] != -1:
                next[prev[curr]] = next[curr]
            if next[curr] != -1:
                prev[next[curr]] = prev[curr]

            # 삭제 후 다음으로 이동 (다음이 없으면 이전으로)
            curr = next[curr] if next[curr] != -1 else prev[curr]
        elif command[0] == 'Z':  # 복구
            idx = removed.pop()
            if prev[idx] != -1:
                next[prev[idx]] = idx
            if next[idx] != -1:
                prev[next[idx]] = idx

    # 최종 상태 문자열 생성
    result = ['O'] * n
    for idx in removed:
        result[idx] = 'X'

    return ''.join(result)
