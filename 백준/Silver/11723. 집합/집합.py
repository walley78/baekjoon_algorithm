import sys
from collections import deque

input = sys.stdin.readline

M = int(input())
numset = set()

for _ in range(M):
    order_num = input().strip().split()
    # 길이가 1이면 명령어만 들어있단 뜻
    if len(order_num) == 1:
        order = order_num[0]
        if order == 'all':
            numset = set(range(1, 21))
        elif order == 'empty':
            numset = set()
    else:
        order, num = order_num[0], int(order_num[1])
        if order == 'add':
            numset.add(num)
        elif order == 'remove':
            if num in numset:
                numset.remove(num)
            else:
                pass
        elif order == 'check':
            if num in numset:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if num in numset:
                numset.remove(num)
            else:
                numset.add(num)