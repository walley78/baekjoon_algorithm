def count_zeros(num):
    cnt = 0
    while num % 10 == 0:
        num //= 10
        cnt += 1
    return cnt

def factorial(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

num = int(input())

factorial_num = factorial(num)
count = count_zeros(factorial_num)

print(count)