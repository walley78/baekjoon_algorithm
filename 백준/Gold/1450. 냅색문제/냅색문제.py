import bisect

def get_sub_sums(arr):
    n = len(arr)
    result = []
    for i in range(1 << n):  # 2^n개의 부분집합
        total = 0
        for j in range(n):
            if i & (1 << j):
                total += arr[j]
        result.append(total)
    return result

N, C = map(int, input().split())
weights = list(map(int, input().split()))

# 1. 반으로 나눈다
left = weights[:N//2]
right = weights[N//2:]

# 2. 각각의 부분집합 합을 구한다
left_sums = get_sub_sums(left)
right_sums = get_sub_sums(right)

# 3. 오른쪽 합을 정렬해 두고
right_sums.sort()

# 4. 왼쪽 합을 기준으로 오른쪽에서 C - l 이하인 원소 개수를 이분 탐색
ans = 0
for l in left_sums:
    remain = C - l
    count = bisect.bisect_right(right_sums, remain)
    ans += count

print(ans)