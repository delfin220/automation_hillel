# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

import abc
class Figure(abc.ABC):
    @abc.abstractmethod
    def area(self): pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    def area(self): return self.__width * self.__height

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
    def area(self): return self.__radius * self.__radius * 3.14

rectangle = Rectangle(100, 200)
circle = Circle(100)
print(circle.area())
print(rectangle.area())