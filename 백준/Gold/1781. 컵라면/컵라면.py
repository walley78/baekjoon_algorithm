import sys
import heapq

input = sys.stdin.readline 

N = int(input())

problems = []

for _ in range(N):
    deadline, ramen = map(int, input().split())
    problems.append((deadline, ramen))

# 데드라인 기준으로 정렬
problems.sort()

heap = [] # min-heap, 먹을 수 있는 라면 수 저장
for d, r in problems:
    # 데드라인 급한 순으로 라면 넣기
    heapq.heappush(heap, r)
    # 근데 만약 heap 리스트의 길이가 데드라인 초과했으면
    if len(heap) > d:
        # 젤 작은 라면 빼기
        heapq.heappop(heap)
        
print(sum(heap))