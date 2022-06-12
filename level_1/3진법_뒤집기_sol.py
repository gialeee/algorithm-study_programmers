def solution(n):
    tmp = ''
    while n:  # n > 0 일때까지만 루프 반복
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)  # int()함수를 이용해서 3진법으로 나타낸 숫자 반환
    return answer
