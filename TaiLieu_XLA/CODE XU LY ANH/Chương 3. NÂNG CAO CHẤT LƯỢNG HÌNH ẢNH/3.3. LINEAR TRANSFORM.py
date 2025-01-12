input()
x = float(input())
y = float(input())
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(n): 
        val = x * a[i][j] + y
        dec = val - int(val)
        if dec > 0.5: a[i][j] = int(val) + 1
        else: a[i][j] = int(val)
        a[i][j] = min(255, a[i][j])
for i in range(n):
    for j in range(n): print(a[i][j], end=" ")
    print()
