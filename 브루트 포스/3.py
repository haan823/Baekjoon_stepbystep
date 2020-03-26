n = int(input())
l = []

for i in range(n):
    l.append(list(map(int, input().split())))

for i in l:
    i.append(1)
    for j in l:
        if i != j:
            if i[0] < j[0] and i[1] < j[1]:
                i[2] += 1
for i in l:
    print(i[2], end=" ")
