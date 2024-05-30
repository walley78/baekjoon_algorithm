import sys

input = sys.stdin.readline

seen, heard = map(int, input().split())

seenset = set()
both = set()

for _ in range(seen+heard):
    name = input().strip()
    if name not in seenset:
        seenset.add(name)
    else:
        both.add(name)

bothlist = list(both)
bothlist.sort()

print(len(bothlist))
for name in bothlist:
    print(name)