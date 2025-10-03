a = list(map(int, input().split()))
s = 1
for i in range(len(a)):
    s = s * a[i]
print(s**(1 / len(a)))