input()
n = int(input())
I = []
for _ in range(n):
    b = list(map(int, input().split()))
    I.append(b)
o = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        old_pixel = I[i][j]
        o[i][j] = 255 if old_pixel >= 127 else 0
        error = old_pixel - o[i][j]
        if j + 1 < n: I[i][j + 1] += error * 7 / 16
        if i + 1 < n and j > 0: I[i + 1][j - 1] += error * 3 / 16
        if i + 1 < n: I[i + 1][j] += error * 5 / 16
        if i + 1 < n and j + 1 < n: I[i + 1][j + 1] += error * 1 / 16
for row in o: print(' '.join(map(str, row)))
