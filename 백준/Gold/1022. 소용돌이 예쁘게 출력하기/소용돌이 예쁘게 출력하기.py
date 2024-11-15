def spiral_value(x, y):
    # 주어진 위치 (x, y)에 대한 소용돌이 숫자를 계산하는 함수
    layer = max(abs(x), abs(y))  # 점의 계층을 결정함 (중심에서의 최대 거리)
    if layer == 0:
        return 1  # 중심점은 항상 1

    # 계층의 길이와 둘레를 계산
    length = 2 * layer
    perimeter = 8 * layer

    # 계층 내 위치에 따라 숫자 계산
    if x == layer and y > -layer:  # 오른쪽 수직선, 위로 이동
        return (2 * layer + 1) ** 2 - (layer - y)
    elif y == -layer and x > -layer:  # 상단 수평선, 오른쪽으로 이동
        return (2 * layer + 1) ** 2 - (2 * layer) - (layer - x)
    elif x == -layer and y < layer:  # 왼쪽 수직선, 아래로 이동
        return (2 * layer + 1) ** 2 - (4 * layer) - (y + layer)
    elif y == layer and x < layer:  # 하단 수평선, 왼쪽으로 이동
        return (2 * layer + 1) ** 2 - (6 * layer) - (x + layer)

import sys
input = sys.stdin.read

r1, c1, r2, c2 = map(int, input().split())

results = []
maxnumlen = 0

# 지정된 범위에 대한 값 생성
for x in range(r1, r2 + 1):
    row = []
    for y in range(c1, c2 + 1):
        val = spiral_value(x, y)  # 각 위치에 대한 값을 계산
        row.append(val)
        maxnumlen = max(maxnumlen, len(str(val)))  # 최대 숫자 길이를 업데이트
    results.append(row)

# 출력 형식을 맞추고 결과를 출력
for row in results:
    print(' '.join(f"{num:>{maxnumlen}}" for num in row))
