from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    # 창고 확장: 상하좌우 1칸씩 여백 추가
    board = [[' ' for _ in range(m + 2)] for _ in range(n + 2)]
    
    for i in range(n):
        for j in range(m):
            board[i + 1][j + 1] = storage[i][j]
    
    for req in requests:
        target = req[0]

        if len(req) == 2:  # 크레인
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if board[i][j] == target:
                        board[i][j] = ' '
        else:  # 지게차: 외부 공기와 연결된 곳만 탐색
            visited = [[False] * (m + 2) for _ in range(n + 2)]
            q = deque()
            q.append((0, 0))
            visited[0][0] = True

            while q:
                x, y = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        if board[nx][ny] == ' ':
                            q.append((nx, ny))
                        elif board[nx][ny] == target:
                            board[nx][ny] = ' '

    # 남은 컨테이너 수 세기
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != ' ':
                answer += 1
    return answer