t = int(input())


def func(n):
    s = [True] * (n + 1)
    s[0] = False
    s[1] = False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if s[i] == True:
            for j in range(2 * i, n + 1, i):
                s[j] = False
    l = []
    dif = n
    for i in range(2, n + 1):
        if s[i] == True:
            l.append(i)
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] + l[j] == n:
                if l[j] - l[i] < dif:
                    a = l[i]
                    b = l[j]
    print(a, b)


for i in range(t):
    n = int(input())
    func(n)
