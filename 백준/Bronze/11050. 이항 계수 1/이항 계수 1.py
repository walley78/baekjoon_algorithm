import sys
input = sys.stdin.readline

def fac1(num):
    result = 1
    for i in range(num, K, -1):
        result *= i

    return result

def fac2(num):
    result = 1
    for i in range(2, num+1):
        result *= i

    return result

N, K = map(int, input().split())

# 이항계수 (N K)는 nCk
# nCk = n! / (n-k)!k!, 단, 0 <= k <= n

ans = fac1(N) / fac2(N-K)


print(int(ans))
