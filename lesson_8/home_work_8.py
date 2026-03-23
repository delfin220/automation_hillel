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

student = Student("Andrii", "Terzeman", 30, 60 )

print(student.get_info())

student.set_average_score(70)
student.name = "test"

print(student.get_info())

