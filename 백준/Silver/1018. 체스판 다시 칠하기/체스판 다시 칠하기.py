# 인터넷 찾아서 답 봄
N, M = map(int, input().split())
chessboard = [list(input()) for _ in range(N)]
# mxn 크기의 하드보드지로 8x8 체스판을 만든다

result = []

for r in range(N-7):    # 이 범위 안에서 +8을 해야 인덱스 범위를 안 벗어남   # 열
    for c in range(M-7):        # 행
        # 시작을 B로 할 때
        draw1 = 0
        # 시작을 W로 할 때
        draw2 = 0

        # 이중 포문 작성
        for a in range(r, r+8):
            for b in range(c, c+8):
                if (a+b) % 2 == 0:      # a, b 를 더한 나머지가 0 => (0, 0), (0, 2) (0, 4) => 인덱스 짝수인 경우뿐임
                    if chessboard[a][b] != "B": # 시작을 B로 할 경우
                        draw1 += 1
                    elif chessboard[a][b] != "W":  # 시작을 W로 할 경우
                        draw2 += 1
                else:               # a, b 를 더한 나머지가 1 => (0, 1), (0, 3), (0, 5) => 인덱스 홀수인 경우뿐임
                    if chessboard[a][b] != "W":  # 시작을 B로 했으면 이쪽 칸들은 무조건 W여야 함
                        draw1 += 1
                    elif chessboard[a][b] != "B":  # 시작을 W로 했으면 이쪽 칸들은 무조건 B여야 함
                        draw2 += 1

        # 포문 다 빠져나오면
        result.append(draw1)
        result.append(draw2)

print(min(result))
