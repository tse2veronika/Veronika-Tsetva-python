s = input().split()
for k in range(len(s)):
    n = s.count(s[k])
    if n == 1:
        print(s[k], end=' ')