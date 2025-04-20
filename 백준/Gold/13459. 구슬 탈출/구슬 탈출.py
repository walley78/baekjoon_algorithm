from collections import deque

# 4방향: 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy, board):
    cnt = 0
    # 벽 만나기 전까지 쭉 굴리기
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(board, rx, ry, bx, by):
    visited = set()
    visited.add((rx, ry, bx, by))
    q = deque()
    q.append((rx, ry, bx, by, 0))  # 마지막은 depth(움직인 횟수)

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            return 0  # 10번 넘으면 실패

        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], board)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], board)

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue
            # 빨간 구슬만 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                return 1

            # 위치가 같으면 겹침 처리 → 더 많이 움직인 쪽을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))

    return 0  # 끝까지 못 빠지면 실패

# 입력 처리
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

print(bfs(board, rx, ry, bx, by))