input()
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(n): a[i][j] = 255 - a[i][j] 
for i in range(n):
    for j in range(n): print(a[i][j], end = " ")
    print()