import sys

def merge_sort(mlist):
    # 계속 쪼갤 수 없을때까지 (length가 1이 될 때까지 쪼개기)
    if len(mlist) == 1:
        return mlist

    # 중간지점 찾아서 왼오 나누기
    mid = len(mlist) // 2
    # 왼 : 리스트의 왼쪽 / 오 : 리스트의 오른쪽
    left = mlist[:mid]
    right = mlist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    # 왼오 병합정렬한거 return
    return merge(left, right)

def merge(left, right):
    # 정렬된거 저장할 빈 리스트
    result = [0] * (len(left) + len(right))

    # left right 인덱스
    l = r = 0
    # 인덱스가 범위 안일때
    while l < len(left) and r < len(right):
        # 왼쪽<오른쪽이면 왼쪽 저장, 반대면 오른쪽 저장
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result



N = int(sys.stdin.readline().rstrip())

numlist = list(int(sys.stdin.readline().rstrip()) for _ in range(N))

result = merge_sort(numlist)

print(*result, sep="\n")