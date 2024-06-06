import sys

input = sys.stdin.readline

# 사람의 수 N
# 각 사람이 돈을 인출하는데 걸리는 시간 P

N = int(input())

times = list(map(int, input().split()))

times.sort()

count = 0

for i in range(N-1, -1, -1):
    count += sum(times)
    times.pop(i)

print(count)