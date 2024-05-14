import sys
input = sys.stdin.readline

# 유클리드 호제법
# x, y의 최대공약수는 y, r의 최대공약수와 같다
# r = x % y (x를 y로 나눈 나머지값)

# 최대공약수 (GCD - Greatest Common Divisor)
def CDG(x, y):
    # while (x%y!=0)
    while (y):
        x, y = y, x%y
    return x

# 최소공배수 (LCM - Least Common Multiple)
def CSG(x, y):
    return ((x*y)//CDG(x, y))


N, M = map(int, input().split())

# 최대공약수
ans1 = CDG(N, M)
print(ans1)

# 최소공배수
ans2 = CSG(N, M)
print(ans2)