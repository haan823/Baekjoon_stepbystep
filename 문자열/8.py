dial = input()
num = 0
for d in dial:
    if d in ["A", "B", "C"]:
        num += 3
    elif d in ["D", "E", "F"]:
        num += 4
    elif d in ["G", "H", "I"]:
        num += 5
    elif d in ["J", "K", "L"]:
        num += 6
    elif d in ["M", "N", "O"]:
        num += 7
    elif d in ["P", "Q", "R", "S"]:
        num += 8
    elif d in ["T", "U", "V"]:
        num += 9
    elif d in ["W", "X", "Y", "Z"]:
        num += 10
print(num)
