n = int(input())
l = []
for i in range(n):
    l.append([])
    m = list(input())
    for j in m:
        l[i].append(j)
score = []
for i, v in enumerate(l):
    score.append([])
    for k, v2 in enumerate(l[i]):
        count = 0
        for j in range(k + 1):
            if l[i][j] == "O":
                count += 1
            else:
                count = 0
        score[i].append(count)
for i in score:
    print(sum(i))
