def solution(n, build_frame):
    structures = []  # 현재 설치된 구조물 (기둥, 보) 정보를 저장하는 리스트

    def is_valid():
        # 현재 설치된 모든 구조물이 규칙을 만족하는지 검사
        for x, y, a in structures:
            if a == 0:  # 기둥일 경우
                if (
                    y == 0  # 바닥 위에 있거나
                    or [x, y - 1, 0] in structures  # 아래에 기둥이 있거나
                    or [x - 1, y, 1] in structures  # 왼쪽에 보가 있거나
                    or [x, y, 1] in structures  # 오른쪽에 보가 있으면
                ):
                    continue
                return False  # 조건을 모두 만족하지 않으면 잘못 설치된 것
            else:  # 보일 경우
                if (
                    [x, y - 1, 0] in structures  # 왼쪽 아래에 기둥이 있거나
                    or [x + 1, y - 1, 0] in structures  # 오른쪽 아래에 기둥이 있거나
                    or ([x - 1, y, 1] in structures and [x + 1, y, 1] in structures)  # 양쪽 모두 보가 연결되어 있으면
                ):
                    continue
                return False  # 조건을 모두 만족하지 않으면 잘못 설치된 것
        return True  # 모든 구조물이 올바르게 설치됨

    for x, y, a, b in build_frame:
        if b == 1:  # 설치하는 경우
            structures.append([x, y, a])
            if not is_valid():
                structures.remove([x, y, a])
        else:  # 삭제하는 경우
            structures.remove([x, y, a])
            if not is_valid():
                structures.append([x, y, a])

    return sorted(structures)  # 최종 결과를 x, y, 구조물 타입 순으로 정렬해 반환
