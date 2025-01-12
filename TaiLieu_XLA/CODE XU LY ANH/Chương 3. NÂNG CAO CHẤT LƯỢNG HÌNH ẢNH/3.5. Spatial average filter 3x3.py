input()
n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b) 

res = []
for i in range(n - 3 + 1):
    tmp = []
    for j in range(n - 2):
        #Ma trận điểm đầu là a[i][j], điểm cuối là a[i + 3][j + 3]
        sub_matrix_sum = 0
        for x in range(3):
            for y in range(3): sub_matrix_sum += a[i + x][j + y]
        tmp.append(round(sub_matrix_sum/9))
    res.append(tmp)

for i in range(n - 2):
    for j in range(n - 2): print(res[i][j], end = " ")
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
