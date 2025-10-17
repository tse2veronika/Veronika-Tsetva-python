N = int(input())
s = input().split()
a = (N - 1) // 2
for i in s:
    count = 0
    for k in s:
        if k < i:
            count += 1
    if count == a:
        print(i)
        break
