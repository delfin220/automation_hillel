#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N

class ReverseIterator:
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


numbers = [10, 20, 30, 40, 50]
reverse_iter = ReverseIterator(numbers)

for num in reverse_iter:
    print(num)


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
ven_iterator = EvenIterator(10)

for i in ven_iterator:
    print(i)

# Напишіть декоратор, який логує аргументи та результати викликаної функції.


def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Викликаємо '{func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Функція '{func.__name__}' повернула: {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b


@log_function
def greet(name, greeting="Привіт"):
    return f"{greeting}, {name}!"



add(5, 3)
print("---")
greet("Андрій")
print("---")
greet(name="Олена", greeting="Вітаю")


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.


def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Помилка в функції '{func.__name__}': {e}")
            return None
    return wrapper


@catch_exceptions
def divide(a, b):
    return a / b

@catch_exceptions
def get_first_element(my_list):
    return my_list[0]

print(divide(10, 2))
print(divide(10, 0))
print(get_first_element([1, 2, 3]))
print(get_first_element([]))
print("Finish")