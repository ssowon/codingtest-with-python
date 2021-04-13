#효율성 검사까지 모두 통과

def solution(participant, completion): 
    answer = ''

    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] != completion[i] :
            answer = participant[i]
            break
    return answer
