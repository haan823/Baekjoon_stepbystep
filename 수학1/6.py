t = int(input())
l = []
for i in range(t):
    l.append(list(map(int, input().split())))
for i in l:
    if i[2] % i[0] == 0:
        print(i[0], end="")
        print("%02d" % (i[2] // i[0]))
    else:
        print(i[2] % i[0], end="")
        print("%02d" % ((i[2] // i[0]) + 1))
