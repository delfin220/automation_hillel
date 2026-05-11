"""
Модуль з кастомними ітераторами.
Містить класи-ітератори для різних задач.
"""


class ReverseIterator:
    """Ітератор для зворотного виведення елементів списку."""

    def __init__(self, my_list):
        self.my_list = my_list
        self.index = len(my_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.my_list[self.index]
        self.index -= 1
        return value

class EvenIterator:
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


if __name__ == "__main__":
    print("=== Тест ReverseIterator ===")
    numbers = [10, 20, 30, 40, 50]
    for num in ReverseIterator(numbers):
        print(num)

    print("\n=== Тест EvenIterator ===")
    for num in EvenIterator(10):
        print(num)