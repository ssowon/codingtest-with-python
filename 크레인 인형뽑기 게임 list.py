from collections import deque
def solution(board, moves):
    answer = 0

    basket = deque()
    depth = len(board)

    for i in moves :
        for j in range(depth) :
            if board[j][i-1] > 0 :
                toy = board[j][i-1]
                board[j][i-1] = 0
                if len(basket) > 0 and basket[-1] == toy:
                    basket.pop()
                    answer += 2
                    break

                else :
                    basket.append(toy)
                    break

    return answer 

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
