#Giả sử size 3x3
n1 = int(input().strip())
SE = []
for _ in range(n1):
    b = list(map(int, input().strip().split()))
    SE.append(b)
n = int(input().strip())
image = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    b = list(map(int, input().split()))
    for j in range(1, n + 1): image[i][j] = b[j - 1]
res = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Kiểm tra vùng SE với tâm tại (i, j)
        for x in range(n1):
            for y in range(n1):
                if SE[x][y] == 1 and image[i + x - 1][j + y - 1] == 1:
                    res[i][j] = 1
                    break
            if res[i][j] == 1: break
for i in range(1, n + 1):
    for j in range(1, n + 1): print(res[i][j], end = ' ')
    print()
