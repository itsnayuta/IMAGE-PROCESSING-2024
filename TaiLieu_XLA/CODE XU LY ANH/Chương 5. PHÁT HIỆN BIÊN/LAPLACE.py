import math
n = int(input())
image = []
for _ in range(n):
    image.append(list(map(int, input().split())))
laplace = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
result = [[0] * n for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        val = 0
        for x in range(3):
            for y in range(3): val+=image[i + x - 1][j + y - 1] * laplace[x][y]
        result[i][j] = abs(val)
for row in result: print(" ".join(map(str, row)))