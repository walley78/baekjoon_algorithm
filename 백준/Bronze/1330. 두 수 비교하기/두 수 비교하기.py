num = list(map(int, input().split()))

A = num[0]
B = num[1]
if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")