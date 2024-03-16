T = int(input()) # test case
# N 총 문서 개수, M 몇번째로 출력되는지 알아보고 싶은 문서 인덱스

for tc in range(T):
    N, M = map(int, input().split())
    numlist = list(map(int, input().split()))
    q = []
    cnt = 0
    for num in enumerate(numlist):
        q.append(num)
    # print(q)

    while q:
        idx, num = q[0]
        max_num = max(numlist)
        if num != max_num:
            q.append(q.pop(0))
        else:
            q.pop(0)
            numlist[idx] = -1
            cnt += 1
            if idx == M:
                break
        # i += 1

    print(cnt)