numbers = list(map(int, input().split()))

A = numbers[0]
B = numbers[1]
C = numbers[2]

print(f"{(A+B)%C}\n{((A%C)+(B%C))%C}\n{(A*B)%C}\n{((A%C) * (B%C))%C}")