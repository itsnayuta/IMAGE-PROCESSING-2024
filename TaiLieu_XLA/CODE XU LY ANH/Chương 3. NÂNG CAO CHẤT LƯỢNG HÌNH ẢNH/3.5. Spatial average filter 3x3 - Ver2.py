input()
n = int(input())

#TH2: Tạo biên --> (n + 2) * (n + 2)
a = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    b = list(map(int, input().split()))
    for j in range(1, n + 1): a[i][j] = b[j - 1]

for i in range(n + 2):
    for j in range(n + 2): print(a[i][j], end = " ")
    print()
print()

res = []
for i in range(n):
    tmp = []
    for j in range(n):
        #Ma trận điểm đầu là a[i][j], điểm cuối là a[i + 3][j + 3]
        sub_matrix_sum = 0
        for x in range(3):
            for y in range(3): sub_matrix_sum += a[i + x][j + y]
        tmp.append(round(sub_matrix_sum/9))
    res.append(tmp)

print("RESULT: ")
for i in range(n):
    for j in range(n): print(res[i][j], end = " ")
    print()
'''
2 7 3 0 
3 1 6 3
0 1 3 5
3 6 7 1

0 0 0 0 0 0
0 2 7 3 0 0
0 3 1 6 3 0
0 0 1 3 5 0
0 3 6 7 1 0
0 0 0 0 0 0
'''
