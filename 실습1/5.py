n = int(input())
count = 0
for i in range(2 * n - 1, 0, -2):
    str = ""
    for j in range(i):
        str += "*"
    for j in range(count):
        print(" ", end="")
    print(str)
    count += 1
count = n - 2
for i in range(3, 2 * n, 2):
    str = ""
    for j in range(i):
        str += "*"
    for j in range(count):
        print(" ", end="")
    print(str)
    count -= 1
