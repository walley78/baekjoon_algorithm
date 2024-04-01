T = int(input())

# 상 하 좌 우 방향
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 블록은 총 5개
# 공이 상하좌우 방향으로 갈때에 맞춰 공이 바뀔 방향 적어두기
# 5개의 블록 방향 정의 (상 하 좌 우)
# 1번 블록
    # 공이 상 : 하
    # 공이 하 : 우
    # 공이 좌 : 상
    # 공이 우 : 좌
# 2번 블록
    # 공이 상 : 우
    # 공이 하 : 상
    # 공이 좌 : 하
    # 공이 우 : 좌
# 3번 블록
    # 공이 상 : 좌
    # 공이 하 : 상
    # 공이 좌 : 우
    # 공이 우 : 하
# 4번 블록
    # 공이 상 : 하
    # 공이 하 : 좌
    # 공이 좌 : 우
    # 공이 우 : 상
# 5번 블록
    # 공이 상 : 하
    # 공이 하 : 상
    # 공이 좌 : 우
    # 공이 우 : 좌
# 0  1  2 3
# 상 하 좌 우
blocks = [
    [],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2],
]

# 범위 안인지 체크하는 함수
def check(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False

# 시작 좌표, 시작 방향
def score_calc(sr, sc, d):
    # 시작 좌표는 기억해둬야함 (다시 시작 좌표로 돌아오면 끝남)
    nr, nc, dir = sr, sc, d
    # 점수 기록할 변수
    score = 0

    # 시작 범위 or 블랙홀 만날때까지 쭉 가자!
    while True:
        # 다음 위치
        nr = nr + direction[dir][0]
        nc = nc + direction[dir][1]
        # 범위 안에 존재하면
        if check(nr, nc):
            # 블록을 만날 경우
            if pinball[nr][nc] in range(1, 6):
                # 점수 증가
                score += 1
                # 블록 타입 뭔지 확인해
                block_type = pinball[nr][nc]
                # 현재 방향에 맞춰서
                dir = blocks[block_type][dir]
                continue
            # 웜홀 만날 경우
            elif pinball[nr][nc] in range(6, 11):
                # 웜홀 다른 쌍으로 보내
                value = pinball[nr][nc]
                if (nr, nc) == wormhole[value][0]:
                    nr, nc = wormhole[value][1]
                else:
                    nr, nc = wormhole[value][0]
                continue
            # 블랙홀 만날 경우
            elif pinball[nr][nc] == -1:
                return score
            # 시작 위치로 돌아왔을 경우
            elif (nr, nc) == (sr, sc):
                return score
        # 범위 밖에 존재하면 (벽을 만났다는 소리)
        else:
            # 점수 추가해
            score += 1
            # 방향 정반대로 바꿔
            if dir == 0:
                dir = 1
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 3
            elif dir == 3:
                dir = 2
            continue


for tc in range(1, T+1):
    # nxn 핀볼판 크기
    N = int(input())
    pinball = [list(map(int, input().split())) for _ in range(N)]

    # 웜홀은 6부터 10의 숫자
    wormhole = [[] for _ in range(11)]
    # 점수 최댓값
    result = 0

    # 웜홀 좌표 찾자 (숫자를 인덱스로 해서 좌표 저장)
    for i in range(N):
        for j in range(N):
            worm = pinball[i][j]
            if worm in range(6, 11):
                wormhole[worm].append((i, j))

    # 0인 곳에서 시작해야함 (0인 곳에서만 갈수있음)
    for i in range(N):
        for j in range(N):
            for d in range(4):
                if pinball[i][j] == 0:
                    score = score_calc(i, j, d)
                    result = max(result, score)

    print(f"#{tc} {result}")
