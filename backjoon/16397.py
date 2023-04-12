"""
버튼 A를 누르면 N이 1 증가한다
버튼 B를 누르면 N에 2가 곱해진 뒤, 0이 아닌 가장 높은 자릿수의 숫자가 1 줄어든다
예를 들어 123→146으로, 5→0으로, 3→5로 변한다
N이 0이면 버튼 B를 눌러도 수가 변하지 않는다.

N이 99,999를 넘어가는 순간 탈출에 실패
B를 눌러 N에 2를 곱한 순간 수가 99,999를 넘어간다면
탈출에 실패

LED로 표현된 N을 G와 같게 만들어야 탈출할 수 있다는 사실

버튼 누르는 횟수를 최소로 하여 방을 탈출
"""
import math
from collections import deque
N, T, G = map(int, input().split())
arr = [math.inf]*100000
q = deque([(N, 0)])
arr[N] = 1
while q:
    n, cnt = q.popleft()
    if cnt >= T:
        continue
    if n == G:
        arr[G] = cnt
        break
    for op in ['a', 'b']:
        new = -1
        if op == 'a':
            if n + 1 > 99999:
                continue
            new = n+1
        else:
            if 0 < n*2 <= 99999:
                new = n*2 - (10**int(math.log10(n*2)))
            else:
                continue
        
        if new >= 0 and arr[new] > cnt + 1:
            arr[new] = cnt + 1
            q.append([new, cnt+1])
    
if arr[G] == math.inf:
    print("ANG")
else:
    print(arr[G])