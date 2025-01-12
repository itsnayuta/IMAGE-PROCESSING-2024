input()  
m, n = list(map(int, input().split()))
x = int(input())  
a = []
for i in range(m):
    b = list(map(int, input().split()))
    a.append(b)

# Bước 1: Đếm tần suất từng mức xám
cnt = [0] * x
for i in range(m):
    for j in range(n): cnt[a[i][j]] += 1

# Bước 2: Tính toán hàm phân phối tích lũy (CDF)
#Khởi tạo
s = [0] * x
mp = [0] * x

s[0] = (x - 1) * cnt[0] / (m * n)
for i in range(1, x): s[i] = s[i - 1] + (x - 1) * cnt[i] / (m * n)
for i in range(x): mp[i] = round(s[i])

# Bước 3: Ánh xạ giá trị cũ sang giá trị mới
for i in range(m):
    for j in range(n): print(mp[a[i][j]], end=" ")
    print()


        