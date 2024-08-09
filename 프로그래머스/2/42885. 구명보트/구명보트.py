def solution(people, limit):
    people.sort(reverse=True)
    fi = 0
    ei = len(people)-1
    count = 0
    while fi <= ei:
        if people[fi] + people[ei] <= limit:
            count += 1
            fi += 1
            ei -= 1
        else:
            count += 1
            fi += 1

    return count
