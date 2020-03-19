n = int(input())
m = n
r = 0
while True:
    n = (n % 10) * 10 + (n // 10 + n % 10) % 10
    r += 1
    if m == n:
        print(r)
        break
