l = []


def hanoi(n, a, b, c):
    if n == 1:
        l.append([a, c])
    else:
        hanoi(n - 1, a, c, b)
        l.append([a, c])
        hanoi(n - 1, b, a, c)


hanoi(int(input()), 1, 2, 3)
print(len(l))
for i in l:
    for j in i:
        print(j, end=" ")
    print()
