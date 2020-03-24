t = int(input())
l = []
m = []
for i in range(t):
    l.append([])
    l[i].append(int(input()))
    l[i].append(int(input()))

for i in range(15):
    m.append([])
    if i == 0:
        for j in range(15):
            m[i].append(j)
    else:
        for j in range(15):
            sum = 0
            for k in range(j + 1):
                sum += m[i - 1][k]
            m[i].append(sum)

for i in range(t):
    print(m[l[i][0]][l[i][1]])
