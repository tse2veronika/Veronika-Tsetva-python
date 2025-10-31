s = input().split()
N = int(s[0])
M = int(s[1])
f = 0
k = 1
while N != 0 or M != 0:
    if N % 2 != 0 and M % 2 != 0:
        f += k
        k *= 4
        N = N // 2
        M = M // 2
    else:
        break
print(f)

