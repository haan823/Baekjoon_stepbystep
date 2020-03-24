import sys

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 <= d and r2 <= d:
            if r1 + r2 > d:
                print(2)
            elif r1 + r2 == d:
                print(1)
            else:
                print(0)
        elif r1 > d or r2 > d:
            if abs(r1 - r2) < d:
                print(2)
            elif abs(r1 - r2) == d:
                print(1)
            else:
                print(0)
