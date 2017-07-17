def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    n = 10
    for i in range(n):
        print(fibonacci(i), end = '  ')

