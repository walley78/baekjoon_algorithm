def solution(operations):
    # min_heap = []
    # max_heap = []
    temp = []
    for op in operations:
        # print(order)
        order = op.split()[0]
        num = int(op.split()[1])
        if order == "I":
            temp.append(num)
            # heapq.heappush(min_heap, num)
            # heapq.heappush(max_heap, (-num, num))
            # heapq.heappush(temp, num)
        else:
            if temp:
                temp.sort()
                if num == 1:
                    # max_num = heapq.heappop(max_heap)[1]
                    # max_idx = temp.index(max_num)
                    temp.pop(len(temp)-1)
                elif num == -1:
                    temp.pop(0)
                    # min_num = heapq.heappop(min_heap)
                    # min_idx = temp.index(min_num)
    temp.sort()
    if temp:
        min_num = temp[0]
        max_num = temp[-1]
        answer = [max_num, min_num]
    else:
        answer = [0, 0]
    return answer