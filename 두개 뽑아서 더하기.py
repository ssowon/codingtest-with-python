def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)-1):
            if i != 1+j:
                answer.append(numbers[i]+numbers[j+1])
    answer = list(set(answer))
    answer.sort()

    return answer
