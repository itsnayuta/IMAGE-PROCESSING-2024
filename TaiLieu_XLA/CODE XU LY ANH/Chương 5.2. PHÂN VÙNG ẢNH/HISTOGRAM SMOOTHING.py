n = int(input())
g = list(map(int, input().split()))
h = list(map(int, input().split()))
def His(w):
    res = []
    k = (w - 1)//2 
    for i in range(n):
        st, en, sum = max(0, i - k), min(n - 1, i + k), 0
        sum = 0 
        for j in range(st, en + 1): sum+=h[j]
        res.append(round(sum/(en - st + 1)))
    print("Smoothed Histogram w={}".format(w))
    for i in range(n): print(i, end = " ")
    print()
    for i in range(n): print(res[i], end = ' ')
    print()
His(3)
His(5)
