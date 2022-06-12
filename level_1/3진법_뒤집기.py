def solution(n):
    answer = 0
    k = 1    
    original_num = []
    
    while n // (3**k - 1) > 0:
        k += 1
    k -= 1
    
    for digit in range(k, -1, -1):
        original_num.append([digit, n // (3**digit)])
        n = n % (3**digit)
    
    reversed_num = sorted(original_num)
    
    for idx in reversed_num:
        answer += idx[1] * 3**(k - idx[0])
    
    return answer
