# функция факториала
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n

# функция предела
def x(n):
    if n == 0:
        return 5.0
    return x(n - 1) / 3.0 - 0.5
print(x(500))

# функция n-ого числа фибоначчи
def fibbonachi_right(n):
    numbers_fib = [0] * n
    numbers_fib[0] = 1
    numbers_fib[1] = 1
    for i in range(2, n):
        numbers_fib[i] = numbers_fib[i - 1] + numbers_fib[i - 2]
    return numbers_fib[-1]
print(fibbonachi_right(8)) #1 задание
