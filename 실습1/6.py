n = int(input())
str1 = ""
str2 = ""
for i in range(1, n + 1):
    if i == 1:
        str1 += "*"
    else:
        if i % 2 == 1:
            str1 += " *"
        else:
            str2 += " *"
if n == 1:
    print(str1)
else:
    for i in range(n):
        print(str1)
        print(str2)
