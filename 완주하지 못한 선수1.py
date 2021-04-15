#효율성 검사 실패 

def solution(participant, completion):
    for i in completion : participant.remove(i)
    answer = participant[0]
    return answer
