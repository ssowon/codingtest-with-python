from collections import deque

def solution(scoville, K):
    answer = 0

    scoville.sort()
    while (scoville[0] < K):
        if len(scoville) < 2 : return -1
        answer += 1
        first = scoville.pop(0)
        second = scoville.pop(0)
        scoville.append(first + second*2)
        scoville.sort()
    return answer

print(solution([1,2,3,9,10,12], 7))