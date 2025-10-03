s = []
n = int(input())
a = 2
while a <= n:
    while n % a == 0:
        s.append(str(a))
        n = n // a
    a += 1
print(' '.join(s))
