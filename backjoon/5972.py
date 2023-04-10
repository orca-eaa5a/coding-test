"""
최소한의 소들을 만나면서 지나가고 싶습니다
N (1 <= N <= 50,000) 개의 헛간과
M (1 <= M <= 50,000) 개의 양방향 길
각각의 길은 C_i (0 <= C_i <= 1,000) 마리의 소
농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N에 있습니다.
"""
import sys
from collections import defaultdict
import heapq
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b ,c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

MAX = 0xfffffffff
dist_tab = [MAX]*(N+1)
stack = []
heapq.heappush(stack, (0, 1))
dist_tab[1] = 0
while stack:
    w, n = heapq.heappop(stack)
    if dist_tab[n] < w:
        continue
    for nw, nn in graph[n]:
        if dist_tab[nn] > w + nw:
            dist_tab[nn] = w + nw
            heapq.heappush(stack, (w + nw, nn))
print(dist_tab[-1])