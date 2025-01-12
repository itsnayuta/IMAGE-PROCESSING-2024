input()
s = input()
n = len(s)
k = 1
for i in range(1, n) :
    if s[i] != s[i - 1] :
        print(str(s[i - 1]) + str(k), end = "")
        k = 1
    else : k += 1
print(str(s[n - 1] + str(k)))