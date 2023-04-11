"""
각 칸은 육지(L)나 바다(W)로 표시
이동은 상하좌우로 이웃한 육지로만 가능하며
보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어
묻혀있다
보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간

보물 지도의 가로, 세로의 크기는 각각 50이하 !!
"""
import sys
from math import inf

def dfs(h, w, arr, start):
    darr = [[inf]*w for _ in range(h)]
    q = [(*start, 0)]
    darr[start[1]][start[0]] = 1
    m = -1
    while q:
        x, y, cnt = q[0]
        del q[0]
        # if darr[y][x] <= cnt and darr[y][x] == 'L':
        #     continue
        if arr[y][x] == 'L':
            for _dx, _dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dx, dy = x + _dx, y + _dy
                if 0 <= dx < w and 0 <= dy < h and arr[dy][dx] == 'L' and darr[dy][dx] > cnt+1:
                    darr[dy][dx] = cnt + 1
                    if darr[dy][dx] > m:
                        m = darr[dy][dx]
                    q.append((dx, dy, cnt + 1))
    return m

h, w = map(int, input().split())
MAX = 0xffffffff
arr = []
for i in range(h):
    arr.append(list(sys.stdin.readline()))

m = -1
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L':
            m = max(m, dfs(h, w, arr, (j, i)))

print(m)
