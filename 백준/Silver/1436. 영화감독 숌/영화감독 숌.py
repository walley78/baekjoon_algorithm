N = int(input())

cnt = 0
start = 665

while cnt < N:
    if '666' in str(start):
        cnt += 1
    start += 1

start -= 1

print(start)