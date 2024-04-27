import sys

# MxN 크기의 집터 / 인벤토리에 B개의 블록 존재
N, M, B = map(int, sys.stdin.readline().split())

# height = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
height = []
for _ in range(N):
    height.extend(list(map(int, sys.stdin.readline().split())))
# print(height)
height_list = list(set(height))
# height_list = list(height_set)

height_dic = {}

for i in height_list:
    height_dic[i] = height.count(i)

# print(height_dic)

# 맨 위의 블록 제거하는 데 2초
# 블록 하나 꺼내서 놓는데 1초

# print(height_list)

max_height = max(height_list)
min_height = min(height_list)

# print(height_set)
# 0, 0, 0 = 시간, 높이, B
time_height = []
min_time = 99999999999999

# 최소 높이와 최대 높이 중 최소 시간이 걸리는 최적의 높이 찾기
for h in range(min_height, max_height+1):
    time = 0
    temp_b = B
    for compare_idx in range(0, len(height_list)):
        # 지금 벽돌 높이 기준으로 맞춰서 시간 재기
        if height_list[compare_idx] != h:
            # 현재 벽돌 높이가 더 크면 깎아야지 (깎는게 2초)
            if height_list[compare_idx] > h:
                time += (height_list[compare_idx]-h)*height_dic[height_list[compare_idx]]*2
                temp_b += (height_list[compare_idx]-h)*height_dic[height_list[compare_idx]]
            # 아니면 쌓아 (그리고 쌓은만큼 인벤토리에서 벽돌 빼고)
            else:
                time += (h-height_list[compare_idx])*height_dic[height_list[compare_idx]]
                temp_b -= (h-height_list[compare_idx])*height_dic[height_list[compare_idx]]
    if temp_b >= 0 and 0 <= h <= 256 and min_time >= time:
        time_height.append((time, h, temp_b))
        min_time = time



# 땅을 고르는 데 걸리는 시간 (작은 순), 땅의 높이 (큰 순) (B는 0 이상이어야 함)
# 시간 높이 B
time_height.sort(key=lambda x: (-x[0], x[1]), reverse=True)

# print(time_height)

ans_time, ans_height, ans_b = time_height[0]

print(f"{ans_time} {ans_height}")


# 둘 중에 작은 시간 쪽으로 정답 출력
# 최소 시간 / 가장 높은 땅 높이