# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(5)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(num1, num2):
    total = num1 + num2
    print("Sum ", total)
sum_numbers(5, 3)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers = [200, 300, 4, 5, 800, 1000]
def average(average):
    return sum(average) / len(average)

result = average(numbers)
print(result)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

entered_text = "test12345"

def reverse_text(text):
    return text[::-1]
print(reverse_text(entered_text))



# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

lst_words = ["text", "Praha", "Test", "lkldjsaldjsalasf", "Ok"]

def check_word(words):
    longest = ""
    for word in words:
        if len(longest) < len(word):
            longest = word
    return longest
print(check_word(lst_words))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calculate_even(numbers_def):
    even = 0
    for number in numbers_def:
        if number % 2 == 0:
            even = even + number
    return even

print(calculate_even(numbers))


# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()


# def unique_symbol(text):
#     unique_symbols = len(set(text))
#     return unique_symbols > 10
#
# text_input = input("Введите текст: ")
# print(unique_symbol(text_input))

# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

def ask_word_with_h():

    text = input("Enter a text: ")
    while "h" not in text.lower():
        print("Has no h or H in:", text)
        text = input("Enter a text: ")
    return text
print(ask_word_with_h())

# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']


def filter_strings(data):
    result = []
    for i in data:
        if isinstance(i, str):
            result.append(i)
    return result
print(filter_strings(lst1))