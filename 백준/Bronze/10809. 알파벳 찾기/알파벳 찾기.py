import string

S = list(input())

alphalist = [-1] * 26

for alpha in S:
    alphalist[string.ascii_lowercase.index(alpha)] = S.index(alpha)


print(*alphalist)