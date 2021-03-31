def solution(prices):
    answer = [1 for i in prices]
    answer[-1] = 0
    keep = [0]
    for i in range(1,len(prices)-1):
        for j in keep[:]:
            if prices[i] >= prices[j] : answer[j] += 1
            else:
                keep.remove(j)
                continue
        keep.append(i)
    return answer
