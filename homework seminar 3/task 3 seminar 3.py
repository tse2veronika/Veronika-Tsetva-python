import math
a, b = map(int, input().split())
d = math.gcd(a, b)
minsum = None
minx = None
miny = None
for x in range(-100000, 100000):
    if (d - a * x) % b == 0:
        y = (d - a * x) // b
        s = abs(x) + abs(y)
        if (minsum is None) or (s < minsum):
            minsum = s
            minx = x
            miny = y
print(minx, miny, d)