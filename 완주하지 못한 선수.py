def solution(participant, completion):
    participant.sort
    for i in completion : participant.remove(i)
    answer = participant[0]
    return answer