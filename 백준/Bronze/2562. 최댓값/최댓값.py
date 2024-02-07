T = 9
numlist = []
for tc in range(9):
    number = int(input())
    numlist.append(number)

print(max(numlist),'\n',numlist.index(max(numlist))+1,end=' ',sep='')