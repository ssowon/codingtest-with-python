from collections import deque
from queue import Queue

def solution(priorities, location):
    print_list = deque([i for i in range(len(priorities))])
    print_deq = deque(priorities)
    result = []

    while len(print_deq) > 1:
        temp = print_deq.popleft()
        paper = print_list.popleft()
        if temp >= max(print_deq) :
            result.append(paper)
        else :
            print_deq.append(temp)
            print_list.append(paper)
    result.append(print_list.popleft())

    return result.index(location)+1



print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1],0))