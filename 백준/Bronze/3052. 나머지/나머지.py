numlist = []
for i in range(10):
    number = int(input())
    numlist.append(number)

for i in range(len(numlist)):
    numlist[i] = numlist[i]%42

numset = set(numlist)
unique = len(numset)

print(unique)