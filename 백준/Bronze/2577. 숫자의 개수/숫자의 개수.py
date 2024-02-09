A = int(input())
B = int(input())
C = int(input())

multiply = A * B * C

mlist = list(str(multiply))
numlist = list(map(int, mlist))

numset = set(numlist)
numdic = {}

for i in range(10):
    numdic[i] = 0

for num in numlist:
    numdic[num] += 1

for num in numdic.values():
    print(num)