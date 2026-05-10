#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.


def even_num(num):
    for i in range(num + 1):
        if i % 2 == 0:
            yield i

for n in even_num(100):
    print(n)

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

for i in fib(100):
    print(i)


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

