n = int(input())
a = 1
b = 1
i = 1
if n == 1:
    print(1)
else:
    while a <= 1000000000:
        a += 1
        b += 6 * i
        if a <= n and b >= n:
            print(i + 1)
            break
        else:
            i += 1
            a = b
            continue
