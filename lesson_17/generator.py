def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("=== Тест even_numbers ===")
    for num in even_numbers(10):
        print(num)

    print("\n=== Тест fibonacci ===")
    for num in fibonacci(100):
        print(num)