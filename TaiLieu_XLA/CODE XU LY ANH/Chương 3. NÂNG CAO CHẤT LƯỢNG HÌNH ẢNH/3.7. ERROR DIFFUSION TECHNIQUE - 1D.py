input()
n = int(input())
I = []
for _ in range(n):
    b = list(map(int, input().split()))
    I.append(b)
e = [[0] * (n) for _ in range(n)]
b = [[0] * (n) for _ in range(n)]
u = [[0] * (n) for _ in range(n)] 

#u sau = I sau - e trước
#e sau = b sau - u sau
'''
VD: u11 = I11, u12 = I12 - e11, u13 = I13 - e12
'''
for i in range(n):
    for j in range(n):
        #Nếu là phần tử đầu tiên của hàng: Không có e trước
        if j==0: u[i][j] = I[i][j]
        else: u[i][j] = I[i][j] - e[i][j - 1]
        #So sánh ngưỡng để suy ra b. Cho ngưỡng = 127. Lớn hơn ngưỡng 255, ngược lại thì 0
        if u[i][j] < 127: b[i][j] = 0
        else: b[i][j] = 255 
        #Tính e
        e[i][j] = b[i][j] - u[i][j]

for i in range(n):
    for j in range(n): print(b[i][j], end = ' ')
    print()