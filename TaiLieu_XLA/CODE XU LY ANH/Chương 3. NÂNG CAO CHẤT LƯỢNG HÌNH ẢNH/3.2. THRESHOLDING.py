input()
k = int(input())
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(n): 
        if a[i][j] <= k: a[i][j] = 0
        else: a[i][j] = 255
for i in range(n):
    for j in range(n): print(a[i][j], end = " ")
    print()