import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []

for r in range(N):
    for c in range(N):
        if cities[r][c] == 2:
            chickens.append((r, c))
        elif cities[r][c] == 1:
            houses.append((r, c))

chickenroadcount = {chicken:dict() for chicken in chickens}

def calcchickenroad():
    for i in range(len(chickens)):
        cr, cc = chickens[i]
        for house in houses:
            hr, hc = house
            distance = (abs(hr-cr) + abs(hc-cc))
            # print(f"해당 치킨집 {(cr, cc)}과 집 {(hr, hc)}와의 거리는 (hr-cr)인 {abs(hr-cr)}와 (hc-cc)인 {abs(hc-cc)}를 더해서 {distance}입니다.")
            chickenroadcount[(cr, cc)][(hr, hc)] = distance

calcchickenroad()

# 골라진 치킨가게들로만 치킨거리 재기
def smallestchickenroad(picked_chickens):
    distance = 0
    for house in houses:
        mindist = float('inf')
        hr, hc = house
        for chicken in picked_chickens:
            cr, cc = chicken
            # print(f"해당 치킨집 {chicken}과 집 {house}와의 거리는 {chickenroadcount[(cr, cc)][(hr, hc)]}입니다")
            mindist = min(mindist, chickenroadcount[(cr, cc)][(hr, hc)])
            # print(f"그래서 최소 거리는 {mindist}입니다.")

        distance += mindist
        # print(f"현재 distance는 방금 계산한 house {house}와의 최소거리 {mindist}를 더해서 {distance} 입니다.")
    return distance


min_distance = float('inf')
# M개의 치킨가게만 골라서 치킨거리 재기
for comb in combinations(chickens, M):
    # print(comb)
    distance = smallestchickenroad(comb)
    min_distance = min(min_distance, distance)

print(min_distance)