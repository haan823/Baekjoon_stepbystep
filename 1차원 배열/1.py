n = int(input())
l = list(map(int, input().split()))
l.sort()
print(l[0], l[n - 1])

