from collections import Counter
import sys
N = int(sys.stdin.readline())

numlist = [0] * N

for _ in range(N):
    num = int(sys.stdin.readline())
    numlist[_] = num
numlist.sort()
numdic = Counter(numlist)
# print(numdic)

# numlist.sort()

# 산술평균
mean_v = sum(numlist)/N
print(round(mean_v))

# 중앙값
median_v = numlist[N//2]
print(median_v)

# 최빈값
# key를 더해라 when? if numdic.values()의 max값(최빈값)이 그 key의 value랑 똑같으면
mode_values = [key for key, value in numdic.items() if value == max(numdic.values())]
if len(mode_values) == 1: # 최빈값이 하나면
    print(mode_values[0])
else: # 최빈값 여러개면
    print(mode_values[1]) # 그 중 2번째로 작은거

# 범위
print(numlist[-1]-numlist[0])