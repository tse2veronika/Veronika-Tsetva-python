n, k = tuple(map(int, input().split()))
A = list(map(int, input().split()))
max = 0
for i in range(2**n):
    j = i ^ k
    sum = A[i] + A[j]
    if sum > max:
        max = sum
print(max)
