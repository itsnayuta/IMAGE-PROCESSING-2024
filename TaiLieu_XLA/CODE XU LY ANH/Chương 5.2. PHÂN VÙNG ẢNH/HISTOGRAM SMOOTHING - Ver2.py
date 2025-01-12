input()
n = int(input())
a, cnt = [], [0] * 100
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
N = -1
for i in range(n):
    for j in range(n): 
        N = max(N, a[i][j])
        cnt[a[i][j]]+=1
print(N)
for i in range(N + 1): print(cnt[i], end = " ")
print()
def His(w):
    res = []
    k = (w - 1)//2 
    for i in range(N + 1):
        st, en, sum = max(0, i - k), min(N, i + k), 0
        sum = 0 
        for j in range(st, en + 1): sum+=cnt[j]
        res.append(round(sum/w))
    print("Smoothed Histogram w={}".format(w))
    for i in range(N + 1): print(i, end = " ")
    print()
    for i in range(N + 1): print(res[i], end = ' ')
    print()
His(3)
His(5)