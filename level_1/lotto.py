def solution(lottos, win_nums):
    answer = []
    zeros = 0
    match = 0
    
    for num in lottos:
        if num == 0:
            zeros += 1
        else:
            if num in win_nums:
                match += 1
            
    highest_rank = 7 - (zeros + match)
    lowest_rank = highest_rank + zeros
    if highest_rank >= 6:
        answer.append(6)
    else:
        answer.append(highest_rank)
    if lowest_rank >= 6:
        answer.append(6)
    else:
        answer.append(lowest_rank)    
    
    return answer
