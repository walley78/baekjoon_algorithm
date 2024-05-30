import sys

input = sys.stdin.readline

# N개의 도감, M개를 맞춰야 함
N, M = map(int, input().split())

pokemon_num = dict()
pokemon_name = dict()

for idx in range(1, N+1):
    name = input().strip()
    pokemon_num[str(idx)] = name
    pokemon_name[name] = str(idx)

# print(pokemon)
# print('=======')

# print(pokemon.keys())

for _ in range(M):
    order_num = input().strip()
    if order_num in pokemon_num.keys():
        print(pokemon_num[order_num])
    else:
        print(pokemon_name[order_num])