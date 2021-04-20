def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        if phone_book[i][0] is not phone_book[i+1][0]:
            continue
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]  :
            return False 
    return answer


phone_book = ["123","456","789"]
print(solution(phone_book))
