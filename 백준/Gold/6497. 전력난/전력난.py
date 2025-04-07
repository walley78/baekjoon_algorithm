import sys

# 재귀 제한 늘리기
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

# Union Find (Disjoint Set)
# x의 부모를 타고 올라가면서 루트 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# a와 b를 같은 집합으로 합치기
# 서로 다른 집합이라면 하나로 합치고 True 반환
# 이미 같은 집합이면 False 반환
# 크루스칼 알고리즘에서 간선 선택 여부를 결정할 때 사용
def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root != b_root:
        parent[b_root] = a_root
        return True
    return False

while True:
    m, n = map(int, input().split())
    if m==0 and n==0:
        break

    # 간선 정보 저장
    edges = []
    # 모든 가로등을 켰을 때의 총 비용
    total_cost = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total_cost += z

    edges.sort() # 비용이 낮은 간선부터 정렬
    # 유니온-파인드용 부모 노드 배열 초기화
    # 초기에는 자기 자신이 부모
    parent = [i for i in range(m)]

    mst_cost = 0
    # 비용이 낮은 간선부터 하나씩 꺼냄
    # a, b가 다른 집합이라면(아직 연결이 안되어 있으면) 간선 선택
    for cost, a, b in edges:
        if union(parent, a, b):
            mst_cost += cost

    print(total_cost-mst_cost)