from collections import deque

def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville = deque(scoville)

    while (scoville[0] < K):
        if len(scoville) < 2 : return -1
        answer += 1
        first = scoville.popleft()
        second = scoville.popleft()
        scoville.append(first + second*2)
        unsorted_scoville = list(scoville)
        unsorted_scoville.sort()
        scoville = deque(unsorted_scoville)
    return answer

print(solution([1,2,3,9,10,12], 7))