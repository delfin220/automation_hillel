# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

def totalsum(numbers):
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total = total + i
    return total

# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()


def count_unique(text):
    unique_symbols = len(set(text))

    if unique_symbols > 10:
        return True
    else:
        return False

# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".



def h_letter(text_input):
    if "h" in text_input.lower():
        return True
    else:
        return False



# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.


class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def set_average_score(self, average_score):
        self.average_score = average_score

    def get_info(self) -> str:
        return f"Student's name:, {self.name} {self.surname}, age: {self.age}, average score: {self.average_score} "
