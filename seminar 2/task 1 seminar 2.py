s = list(map(int, input().split()))
print(int(s[0] * (s[0] + 1) / 2 - (sum(s) - s[0])))