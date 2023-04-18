"""
숫자 0이 적힌 블록들이 설치된 도로에 다른 숫자가 적힌 블록들을 설치
길이가 1,000,000,000인 도로에 
1부터 10,000,000까지의 숫자가 적힌 블록들을 이용해 위의 규칙대로 모두 설치 
"""
def get_p(n):
    lim = 10000000
    if n == 1:
        return 0
    last_biggest_prime = 1
    for i in range(2, int((n)**0.5)+1):
        if n%i == 0:
            last_biggest_prime = i
            if n//i <= lim:
                last_biggest_prime = n//i
                return last_biggest_prime
        if n%i == 0 and n//i <= lim:
            return n//i
    return last_biggest_prime
def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(get_p(i))
    
    return answer

if __name__ == '__main__':
    solution(
        100000015, 100000015
    )