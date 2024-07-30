import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        small1 = heapq.heappop(scoville)
        if small1 < K:
            small2 = heapq.heappop(scoville)
            new = small1 + (small2 * 2)
            heapq.heappush(scoville, new)
            count += 1

    return count