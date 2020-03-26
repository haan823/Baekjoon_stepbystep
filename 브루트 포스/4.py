n, m = map(int, input().split())
min_num = n * m

l1 = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]

l2 = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]

l = []

for i in range(n):
    l.append(list(input()))


for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for y in range(i, i + 8):
            for x in range(j, j + 8):
                if l[y][x] != l1[y - i][x - j]:
                    cnt1 += 1
                if l[y][x] != l2[y - i][x - j]:
                    cnt2 += 1
        if cnt1 >= cnt2:
            if cnt2 < min_num:
                min_num = cnt2
        elif cnt1 < cnt2:
            if cnt1 < min_num:
                min_num = cnt1

print(min_num)
