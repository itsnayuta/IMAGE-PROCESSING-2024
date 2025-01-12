input()
n = int(input())  
a = []  
cnt, p, rp = [0] * 256, [0] * 256, [0] * 256  
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(n): cnt[a[i][j]] += 1
for i in range(256):
    if cnt[i]:  
        p[i] = cnt[i] / (n * n)  
        rp[i] = i * p[i]  
t0 = sum(rp)  
epsilon = 0.001  
while True:
    lower_s, lower_w = 0, 0
    upper_s, upper_w = 0, 0
    for i in range(256):
        if i <= t0:
            lower_s += rp[i]
            lower_w += p[i]
        else:
            upper_s += rp[i]
            upper_w += p[i]
    if lower_w > 0: mean_lower = lower_s / lower_w 
    else: mean_lower = 0
    if upper_w > 0: mean_upper = upper_s / upper_w
    else: mean_upper = 0
    t1 = (mean_lower + mean_upper) / 2
    if abs(t1 - t0) < epsilon: break
    t0 = t1
print(f"Isodata threshold = {int(t1)}")
