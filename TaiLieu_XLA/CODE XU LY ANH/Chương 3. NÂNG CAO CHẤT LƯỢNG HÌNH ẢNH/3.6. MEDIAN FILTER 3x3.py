# Đọc kích thước của ma trận
input()
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
res = []

for i in range(n - 2):
    tmp1 = []
    for j in range(n - 2):
        tmp = []
        for x in range(3):
            for y in range(3): tmp.append(a[i + x][j + y])
        tmp.sort()
        tmp1.append(tmp[4])
    res.append(tmp1)

for i in range(n - 2):
    for j in range(n - 2): print(res[i][j], end = " ")
    print()

