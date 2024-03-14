# For any prime number greater than 3, it must be of the form 6k ± 1. This is because all primes greater than 3 can be represented as either a multiple of 6 plus or minus 1. Primes like 5 (6 * 1 - 1) and 7 (6 * 1 + 1) follow this pattern.
# Sieve of Eratosthenes (에라토스테네스의 체)

def prime(num):
    if num <= 1:
        return False # 1 이하는 소수가 아님
    if num <= 3:
        return True # 1 초과 3 이하면 2, 3 = 소수
    if num % 2 == 0 or num % 3 == 0:
        return False # 2나 3으로 나눠지면 소수가 아님
    i = 5
    # 3 이후의 모든 소수는 6k+1이거나 6k-1이다.
    while i*i <= num: # i 제곱이 숫자보다 작은 동안
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6 # 6을 더해준다 (6의 배수 + 1 아니면 -1 이니까)
    return True

min, max = map(int, input().split())

primenum = [num for num in range(min, max+1) if prime(num)]

print(*primenum, sep='\n')