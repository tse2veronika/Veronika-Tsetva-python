s = input().split()
n = 0
for k in range(len(s)):
    if s.count(s[k]) > n:
        n = s.count(s[k])
        a = s[k]
print(a)