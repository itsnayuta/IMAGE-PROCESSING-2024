input()
n1 = int(input())
SE = []
for _ in range(n1):
    b = list(map(int, input().split()))
    SE.append(b)
n = int(input())
image = []
for _ in range(n):
    b = list(map(int, input().split()))
    image.append(b)
# Bước 1: Co ảnh (erosion)
res = [[0] * n for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        check = 1
        for x in range(n1):
            for y in range(n1):
                if SE[x][y] == 1 and image[i + x - 1][j + y - 1] == 0:
                    check = 0
                    break
            if check == 0: break
        res[i][j] = check

# Bước 2: Ảnh biên = Ảnh gốc - Ảnh co
ans = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n): ans[i][j] = image[i][j] - res[i][j]
for row in ans: print(" ".join(map(str, row)))
