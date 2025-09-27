f = open('input6.txt')
a = f.readlines()
s = list(map(int, a[0].split()))
c = int(a[2])
b = 0
d = []
w = 1
g = 0
for k in range(len(s)):
    q = len(str(s[k]))
    for i in range(q):
        b += int(str(s[k])[i]) * (c ** (q - 1))
        q -= 1
    d.append(b)
    b = 0
if a[1] == '+\n':
    for l in range(len(d)):
        b += d[l]
elif a[1] == '-\n':
    for l in range(len(d)):
        b -= d[l]
elif a[1] == '*\n':
    for l in range(len(d)):
        w *= d[l]
if b != 0:
    g = b
else:
    g = w
t = []
while g != 0:
    t.append(str((g % c)))
    g = g // c
t = t[::-1]
y = ''.join(t)
f = open('output6.txt', 'w')
f.write(y)
f.close()
