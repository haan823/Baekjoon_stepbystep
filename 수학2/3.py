m, n = map(int, input().split())
s = [True] * (n + 1)
s[0] = False
s[1] = False
l = int(n ** 0.5)
for i in range(2, l + 1):
    if s[i] == True:
        for j in range(2 * i, n + 1, i):
            s[j] = False
for i in range(m, n + 1):
    if s[i] == True:
        print(i)
