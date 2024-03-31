import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0

# 어차피 5 아님 3으로 나눠져야 함
# 5로 먼저 다 나누면 3으로 안 나눠질 가능성이 있음
# 숫자가 5이 배수가 될때까지 3을 뺄것
while N > 0:
    if N >= 3 and N%5 != 0:
        N -= 3
        cnt += 1
    elif N%5 == 0:
        cnt += (N//5)
        N %= 5
        break
    else:
        break

if N == 0:
    print(cnt)
else:
    print(-1)