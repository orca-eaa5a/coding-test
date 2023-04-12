"""
PT를 한 번 받을 때 운동기구를 최대 두 개까지만 선택할 수 있다.
N개의 운동기구, 이전에 사용하지 않았던 운동기구를 선택하기로 계획
비용을 절약하기 위해 PT를 받을 때 운동기구를 되도록이면 두 개를 사용
PT를 한 번 받을 때의 근손실 정도가 M을 넘지 않도록
근손실 정도는 두 운동기구의 근손실 정도의 합

M의 최솟값
"""
import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
m = 0xfffffff
if N % 2 == 0:
    for i in range(N//2):
        m = max(m, arr[i] + arr[N-1-i])
else:
    m = arr[-1]
    for i in range((N-1)//2):
        m = max(m, arr[i] + arr[N-2-i])
print(m)

"""
1 2 3 4 5 6

3 5 9 11 20 21

"""