import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    order_num = input().strip().split()

    if len(order_num) == 1:
        order = order_num[0]
        if order == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif order == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
        elif order == 'size':
            print(len(queue))
        elif order == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif order == 'pop':
            if queue:
                front = queue.popleft()
                print(front)
            else:
                print(-1)
    else:
        order, num = order_num[0], order_num[1]
        if order == 'push':
            queue.append(num)