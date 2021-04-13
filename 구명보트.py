def solution(people, limit):
    answer = 0
    people.sort()
    print(people)
    start = 0
    last = len(people)-1
    for i in range(len(people)):
        if start == last :
            answer += 1
            break
        elif start > last :
            break
        if people[start]+people[last] > limit:
            last -= 1
            answer += 1
        else :
            start += 1
            last -= 1
            answer += 1


    return answer

print(solution([70, 50, 80, 50], 100)) #3
print(solution([70, 80, 50], 100)) #3
