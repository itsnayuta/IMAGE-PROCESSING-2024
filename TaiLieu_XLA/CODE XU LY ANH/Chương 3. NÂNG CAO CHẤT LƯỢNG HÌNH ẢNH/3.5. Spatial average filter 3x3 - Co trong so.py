n = int(input())

#Giả sử hệ số chia là 16
#TH2: Tạo biên ma trận A--> (n + 2) * (n + 2)
a = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    b = list(map(int, input().split()))
    for j in range(1, n + 1): a[i][j] = b[j - 1]

#Nhập ma trận cửa sổ nhân chập
c = []
for i in range(3):
    d = list(map(int, input().split()))
    c.append(d)

res = []
for i in range(n):
    tmp = []
    for j in range(n):
        #Ma trận điểm đầu là a[i][j], điểm cuối là a[i + 3][j + 3]
        sub_matrix_sum = 0
        for x in range(3):
            for y in range(3): sub_matrix_sum += a[i + x][j + y] * c[x][y]
        tmp.append(round(sub_matrix_sum/16))
    res.append(tmp)

print("RESULT: ")
for i in range(n):
    for j in range(n): print(res[i][j], end = " ")
    print()
'''
4
1 2 3 2
4 16 2 1
4 2 1 1
2 1 2 1
1 2 1
2 4 2
1 2 1
'''
