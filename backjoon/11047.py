"""
동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고
동전을 적절히 사용해서 그 가치의 합을 K로
동전 개수의 최솟값
"""
import sys
N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

cnt = 0
for e in coins[::-1]:
    if K//e > 0:
        cnt += K//e
        K -= (e*(K//e))
print(cnt)
    