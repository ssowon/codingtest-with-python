def solution(n):
    answer = ''
    n -= 1
    
    while n > 2 :
        answer += str(n % 3)
        if n // 3 == 3 :
            answer += str(3)
            break
        n = n//3
    else :
        answer += str(n)
    if len(answer) == 1 :
        answer = answer.replace('2','4').replace('1','2').replace('0','1')
    else :
        answer = answer[0].replace('2','4').replace('3','4').replace('0','1') + answer[1:].replace('3','4')
    return answer[::-1]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
print(solution(14))
print(solution(15))
