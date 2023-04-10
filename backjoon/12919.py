"""
두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
1. 문자열의 뒤에 A를 추가
2. 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성

1 ≤ S의 길이 ≤ 49, 2 ≤ T의 길이 ≤ 50
S의 길이 < T의 길이

S를 T로 바꿀 수 있으면 1을 없으면 0을 출력
"""
from collections import deque

"""
- 실행시간 초과
v----초기 코드
"""
# def bfs(S, T):
#     Tlen = len(T)
#     q = set()
#     q.add((S, len(S)))
#     while q:
#         s, l = next(iter(q))
#         q.discard((s, l))
#         if l > Tlen:
#             continue
#         elif l == Tlen:
#             if s == T:
#                 return 1
#         else:
#             for op in ['a', 'b']:
#                 if op == 'a':
#                     q.add((s+"A", l+1))
#                 elif op == 'b':
#                     q.add(((s+"B")[::-1], l+1))
#     return 0


"""
실행시간을 줄이기 위한 핵심 아이디어 -> T를 줄여나가자
아마 문자열 비교에서 실행시간이 많이 소모되는 듯?
좋은 문제는 아닌거 같은데...
"""
def bfs(S, T):
    slen = len(S)
    q = set()
    q.add((T, len(T)))
    while q:
        v = next(iter(q))
        q.discard(v)
        t, l = v
        if slen > l:
            continue
        elif slen == l:
            if t == S:
                return 1
            continue
        else:
            for op in ['a', 'b']:
                if t[-1] == 'A':
                    q.add((t[:-1], l-1))
                if t[0] == 'B':
                    q.add((t[1:][::-1], l-1))
    return 0

S = input()
T = input()

print(bfs(S, T))