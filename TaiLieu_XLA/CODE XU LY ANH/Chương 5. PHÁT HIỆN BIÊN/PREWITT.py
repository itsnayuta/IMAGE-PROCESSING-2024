import math
n = int(input())
image = []
for _ in range(n):
    image.append(list(map(int, input().split())))

# Bộ lọc Prewitt theo X và Y
prewitt_x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
prewitt_y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]

result = [[0] * n for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        Gx, Gy = 0, 0
        for x in range(3):
            for y in range(3):
                Gx += image[i + x - 1][j + y - 1] * prewitt_x[x][y]
                Gy += image[i + x - 1][j + y - 1] * prewitt_y[x][y]
        G = math.sqrt(Gx**2 + Gy**2)
        result[i][j] = int(G)
for row in result: print(" ".join(map(str, row)))