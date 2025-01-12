import math
n = int(input())
img = []
for _ in range(n):
    img.append(list(map(int, input().split())))
res = [[0] * n for _ in range(n)]
for i in range(n - 1):
    for j in range(n - 1):
        Gx = img[i][j] - img[i + 1][j + 1]
        Gy = img[i + 1][j] - img[i][j + 1]
        G = math.sqrt(Gx**2 + Gy**2)
        res[i + 1][j + 1] = int(G)
for i in range(n):
    res[i][n - 1] = 0
    res[n - 1][i] = 0
for row in res: print(" ".join(map(str, row)))

