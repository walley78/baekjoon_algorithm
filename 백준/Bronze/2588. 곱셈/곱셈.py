A = int(input())
B = int(input())
splited = list(str(B))
splited.reverse()

splitedint = list(map(int, splited))
for num in splitedint:
    print(A*num)

print(A*B)