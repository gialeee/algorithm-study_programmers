def solution(n):
    tmp = ''
    while n:  # n > 0 일때까지만 루프 반복
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)  # int(value, base) 함수를 이용해서 3진법으로 나타낸 숫자 반환
                          # value : string 또는 number을 int형으로 변환
                          # base : 넘버 포맷(n진법)을 결정 / default : 10
    return answer
