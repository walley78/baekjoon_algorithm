import sys

input = sys.stdin.readline

# 티셔츠는 6가지 사이즈
# 같은 사이즈의 T장 묶음으로만 주문 가능
# 남아도 되지만 부족해서는 안됨

# 펜은 P자루씩 묶음으로 주문하거나 한 자루씩 주문
# 남아도 부족해도 안됨 정확해야함

# 티셔츠 T장씩 최소 몇 묶음? 펜은 P자루씩 최대 몇 묶음? 한자루씩 몇개?

# 참가자 수 N
participants = int(input())

# 티셔츠 사이즈별 신청자의 수 공백으로
tshirts = list(map(int, input().split()))

# 티셔츠 묶음 수 T 그리고 펜의 묶음 수 P
T, P = map(int, input().split())

# 펜은 사이즈가 따로 없음
# 총 참가자 수 // P 묶음, 그리고 총 참가자 수 % P 자루
pen_bundle = participants // P
pen_separate = participants % P

# 티셔츠
# 사이즈별로 작거나 같으면 +1, 크면 // 하고 + 1 (T보다 작은 나머지가 있을테니까)
t_cnt = 0
for size in tshirts:
    t_cnt += (size+T-1) // T

print(t_cnt)
print(f"{pen_bundle} {pen_separate}")