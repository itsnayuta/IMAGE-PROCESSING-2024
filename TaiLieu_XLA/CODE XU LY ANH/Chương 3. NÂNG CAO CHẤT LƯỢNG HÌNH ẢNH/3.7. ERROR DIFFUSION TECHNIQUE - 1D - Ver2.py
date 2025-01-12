n, m = map(int, input().split())
I = []
for _ in range(n):
    b = list(map(int, input().split()))
    I.append(b)
e = [[0] * m for _ in range(n)]
b = [[0] * m for _ in range(n)]
u = [[0] * m for _ in range(n)]
threshold = 127
for i in range(n):
    for j in range(m):
        if j == 0: u[i][j] = I[i][j]
        else: u[i][j] = I[i][j] - e[i][j - 1]
        if u[i][j] < threshold: b[i][j] = 0
        else: b[i][j] = 255
        e[i][j] = b[i][j] - u[i][j]
for i in range(n):
    for j in range(m): print(b[i][j], end=' ')
    print()
