K, N = map(int, input().split())
lines = []

for _ in range(K):
    num = int(input())
    lines.append(num)

# 방법은 이분탐색 (중간 잘라서 찾으려는 값이 중간보다 작으면 중간-1을 새로운 끝으로 설정, 크면 중간+1을 새로운 시작으로 설정)

start, end = 1, max(lines) # 랜선의 최대 길이는 가진 랜선들의 최댓값, 제일 작을 수 있는 랜선의 길이는 1

while start <= end: # start가 end보다 작은 동안 실행
    mid = (start + end) // 2 # 중간값 시작
    value = 0 # 우리가 찾는 N개 (이상)를 만들수있는 랜선의 최대 길이
    for line in lines:
        value += line // mid # 현재의 중간값으로 가진 랜선에서 몇개나 만들수있음?

    if value >= N: # 우리가 찾은 길이로 만들수있는 랜선이 N개가 넘어가면 랜선 길이를 좀 더 늘려본다 (최대 랜선의 길이를 찾아야 하니까)
        start = mid + 1
    else: # 만들수 있는 랜선의 길이가 N개 이하면 랜선 길이를 줄여본다
        end = mid - 1

# while 문 빠져나오면 N 만드는 최대길이 랜선 찾았다는 소리
# 그때의 start랑 end로 mid 다시 한번 계산
mid = (start + end) //2

print(mid)