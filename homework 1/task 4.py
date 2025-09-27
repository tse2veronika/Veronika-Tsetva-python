f = open('input.txt')
a = f.readlines()
s = list(map(int, a[0].split()))
b = 0
d = 1
if a[1] == '+':
    for i in range(len(s)):
        b += s[i]
elif a[1] == '-':
    for i in range(len(s)):
        b -= s[i]
elif a[1] == '*':
    for i in range(len(s)):
        d *= s[i]
f = open('output.txt', 'w')
if b != 0:
    f.write(str(b))
else:
    f.write(str(d))
f.close()
