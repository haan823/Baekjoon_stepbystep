def func(n):
    s = [True] * ((2 * n) + 1)
    s[0] = False
    s[1] = False
    m = int((2 * n) ** 0.5)
    for i in range(2, m + 1):
        if s[i] == True:
            for j in range(2 * i, (2 * n) + 1, i):
                s[j] = False
    result = []
    for i in range(n + 1, (2 * n) + 1):
        if s[i] == True:
            result.append(i)
    return len(result)


while True:
    n = int(input())
    if n == 0:
        break
    print(func(n))
