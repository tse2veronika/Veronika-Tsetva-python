import math
n, s = tuple(input().split())
n = int(n)
if n % 2 == 0:
    for i in range(n // 2):
        print((i + 1) * s)
    for i in range(n // 2, 0, -1):
        print(i * s)
else:
    l = math.ceil(n / 2)
    for i in range(l):
        print((i + 1) * s)
    for i in range(n - l, 0, -1):
        print(i * s)