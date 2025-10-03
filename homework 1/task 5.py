N = int(input())
b = int(input())
c = int(input())
n = str(N)
s = len(n)
A = 0
for k in range(s):
    A += int(n[k]) * (b ** (s - 1))
    s -= 1
d = []
while A != 0:
    d.append(str((A % c)))
    A = A // c
d = d[::-1]
f = ''.join(d)
print(int(f))
