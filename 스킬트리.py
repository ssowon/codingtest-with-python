def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees :
        num = 0
        for j in i:
            if j == skill[num] : num += 1
            elif j in skill and j != skill[num]: break

            if len(skill) <= num or i[-1] == j:
                answer += 1
                break

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))