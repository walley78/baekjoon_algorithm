import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

d = deque()

for _ in range(N):
    order_num = input().strip().split()

    if len(order_num) == 1:
        order = order_num[0]
        if d:
            if order == 'pop_front':
                front = d.popleft()
                print(front)
            elif order == 'pop_back':
                back = d.pop()
                print(back)
            elif order == 'size':
                print(len(d))
            elif order == 'empty':
                print(0)
            elif order == 'front':
                print(d[0])
            elif order == 'back':
                print(d[-1])
        else:
            if order == 'empty':
                print(1)
            elif order == 'size':
                print(len(d))
            else:
                print(-1)
    else:
        order, num = order_num[0], order_num[1]
        if order == 'push_front':
            d.appendleft(num)
        elif order == 'push_back':
            d.append(num)
        