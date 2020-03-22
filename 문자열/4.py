t = int(input())
l = []
num = []
m = []
for i in range(t):
    l.append(input().split())
    num.append(int(l[i].pop(0)))
    l[i] = list(l[i][0])
for i in range(t):
    m.append([])
    for j in l[i]:
        for k in range(num[i]):
            m[i].append(j)
    print("".join(m[i]))
