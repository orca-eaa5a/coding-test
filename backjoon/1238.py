import sys
from collections import defaultdict

N, M, X = map(int, input().split())

# graph = defaultdict(list)
# for _ in range(M):
#     s, d, w = map(int, sys.stdin.readline().split())
#     graph[s].append((w, d))
MAX = 0xffffffff
graph = [[MAX]*N for _ in range(N)]
for _ in range(M):
    s, d, w = map(int, sys.stdin.readline().split())
    graph[s-1][d-1] = w

for c in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][b] > graph[a][c] + graph[c][b]:
                graph[a][b] = graph[a][c] + graph[c][b]

m = -1
for i in range(N):
    m = max(m, graph[i][X-1] + graph[X-1][i])
print(m)