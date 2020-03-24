x = int(input())
i = 1
while x > 0:
    x -= i
    i += 1
if i % 2 != 0:
    print(str(x + i - 1) + "/" + str(1 - x))
else:
    print(str(1 - x) + "/" + str(x + i - 1))
