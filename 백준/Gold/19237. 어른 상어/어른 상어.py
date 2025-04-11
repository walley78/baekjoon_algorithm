n, m, k = map(int, input().split())

# 격자 정보: 각 칸에 있는 상어 번호 (0은 빈 칸)
data = [list(map(int, input().split())) for _ in range(n)]

# 상어의 현재 방향 (1~4) → 0-index로 바꾸어 저장
directions = list(map(int, input().split()))
directions = [d-1 for d in directions]

# 각 상어의 방향 우선순위: m개 상어, 각 4방향마다 4개의 우선순위
priorities = []
for _ in range(m):
    temp = []
    for _ in range(4):
        row = list(map(int, input().split()))
        temp.append([d-1 for d in row])  # 0-index 변환
    priorities.append(temp)

# 냄새: 각 칸에 (상어번호, 남은시간)
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

# 방향 벡터: 위, 아래, 왼쪽, 오른쪽 (0-index)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 냄새 갱신
def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], k]

# 상어 이동
def move():
    new_data = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                shark_num = data[x][y]
                dir = directions[shark_num-1]
                moved = False

                # 냄새 없는 칸 우선
                for d in priorities[shark_num-1][dir]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            directions[shark_num-1] = d
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = shark_num
                            else:
                                new_data[nx][ny] = min(new_data[nx][ny], shark_num)
                            moved = True
                            break

                if moved:
                    continue

                # 자기 냄새 칸
                for d in priorities[shark_num-1][dir]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == shark_num:
                            directions[shark_num-1] = d
                            new_data[nx][ny] = shark_num
                            break
    return new_data

# 메인 시뮬레이션
time = 0
while True:
    update_smell()
    data = move()
    time += 1

    # 종료 조건: 1번 상어만 남았는지 확인
    alive = [data[i][j] for i in range(n) for j in range(n) if data[i][j] > 0]
    if alive.count(1) == len(alive):
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
