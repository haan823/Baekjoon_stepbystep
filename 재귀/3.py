n = int(input())
l = ["***", "* *", "***"]


def star(n):
    if n == 3:
        return l
    else:
        m = []
        o = star(n // 3)
        for i in range(n):
            m.append(o[i % (n // 3)])
        for i in range(n):
            if i // (n // 3) == 1:
                tmp = m[i]
                for _ in range(n // 3):
                    m[i] += " "
                m[i] += tmp
            else:
                m[i] *= 3
        return m


for i in star(n):
    print(i)
