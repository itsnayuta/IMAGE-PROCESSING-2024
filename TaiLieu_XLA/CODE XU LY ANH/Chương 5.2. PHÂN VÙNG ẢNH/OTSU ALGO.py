
n, N = int(input()), -1  
a, cnt = [], [0] * 256 
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    for j in range(n):
        cnt[a[i][j]] += 1
        N = max(N, a[i][j])  

# Tính xác suất p[i], xác suất tích lũy P[i], và m[i] (tích lũy mức xám)
p, P, m, mG = [0] * 256, [0] * 256, [0] * 256, 0
p[0] = cnt[0] / (n * n)  # Xác suất mức xám 0
P[0] = p[0]  
for i in range(1, N + 1):
    p[i] = cnt[i] / (n * n)  # Xác suất của mức xám i
    P[i] = P[i - 1] + p[i]  # Tích lũy xác suất đến mức xám i
    m[i] = m[i - 1] + i * p[i]  # Tích lũy mức xám (i * xác suất của mức xám i)
mG = m[N]  # Tổng mức xám của toàn ảnh

threshold = 0  # Ngưỡng tối ưu ban đầu
res = -1  # Phương sai tối đa ban đầu
for i in range(0, N + 1):
    if P[i] == 0 or P[i] == 1: continue
    tu = mG * P[i] - m[i]  
    mau = P[i] * (1 - P[i]) 
    if round(tu * tu / mau, 2) > res:  
        res = round(tu * tu / mau, 2)
        threshold = i  
print(f"Otsu threshold = {threshold}")
