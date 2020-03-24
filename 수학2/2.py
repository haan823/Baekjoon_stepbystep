m = int(input())
n = int(input())
s = [True] * (n + 1)
l = int(n ** 0.5)
s[0] = False
s[1] = False
for i in range(2, l + 1):
    if s[i] == True:
        for j in range(i * 2, n + 1, i):
            s[j] = False
result = []
for i in range(m, n + 1):
    if s[i] == True:
        result.append(i)
if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
