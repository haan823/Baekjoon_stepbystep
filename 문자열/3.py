s = list(input())
for i in range(ord("a"), ord("z") + 1):

    if chr(i) not in s:
        print(-1, end=" ")
    else:
        for j, v in enumerate(s):
            if ord(v) == i:
                print(j, end=" ")
                break
