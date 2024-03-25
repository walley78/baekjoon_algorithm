from collections import deque

N = int(input())

numlist = deque([i for i in range(1, N+1)])
idx = 0
# queue = deque()
# queue.append(numlist[idx])
result = 0
while numlist:
    if idx % 2 == 0:
        idx += 1
        result = numlist.popleft()
    else:
        result = nb = numlist.popleft()
        idx += 1
        numlist.append(nb)

print(result)

# while idx < N:
#     idx += 2
#     if idx < N:
#         numlist[idx], numlist[N-1] = numlist[N-1], numlist[idx]
#
# print(numlist[-1])

# 1부터 N까지의 번호
# 1이 제일 위에, N이 제일 밑에

# def bottom(start, end):
#     if start == N+2:
#         return start+1
#     elif start == N:
#         return end
#     bottom(start+2, start+1)
#
# bottom(1, N)