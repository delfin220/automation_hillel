from iterator import ReverseIterator, EvenIterator
from generator import even_numbers, fibonacci
from decorator import log_function, catch_exceptions


@log_function
@catch_exceptions
def divide(a, b):
    return a / b


if __name__ == "__main__":
    print("=== Використання ітераторів ===")
    for num in EvenIterator(10):
        print(num, end=" ")
    print()

    print("\n=== Використання генераторів ===")
    for num in fibonacci(50):
        print(num, end=" ")
    print()

    print("\n=== Використання декораторів ===")
    divide(10, 2)
    divide(10, 0)