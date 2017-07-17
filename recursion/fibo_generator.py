def fibo(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = 10
    f = fibo(n)
    print(f)

    for i in range(n):
        print(next(f), end = '  ')

