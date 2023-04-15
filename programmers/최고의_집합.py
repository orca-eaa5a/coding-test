"""
4, 9
2, 2, 2, 3 -> 24
1, 2, 3, 4 -> 20
2, 3, 3, 1 -> 18
1, 3, 3, 1 -> 9
"""
def solution(n, s):
    answer = []
    if s%n == 0:
        answer = [s//n]*n
    else:
        _mid = s//n
        if _mid != 0:
            answer = [_mid]*n
            for i in range(s%n):
                answer[i] += 1
            answer.sort()

        else:
            answer = [-1]

    return answer