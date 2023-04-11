N = int(input())

arr = []
arr2 = [[0]*N for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    stack = [i]
    while stack:
        y = stack.pop()
        for n, e in enumerate(arr[y]):
            if e == 1 and arr2[i][n] == 0:
                arr2[i][n] = 1
                stack.append(n)

for row in arr2:
    print(" ".join(list(map(str, row))))