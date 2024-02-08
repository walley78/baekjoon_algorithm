numlist = list(map(int, input().split()))

number = numlist[0]
numsquare = number**2

for num in numlist[1:]:
    numsquare += num**2

numdivide = numsquare%10
print(numdivide)