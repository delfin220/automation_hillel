
# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Romb:
    def __init__(self, side_a: float, corner_a: float):
        self.side_a = side_a
        self.corner_a = corner_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side cannot be less than or equal to 0")
            super().__setattr__(name, value)

        elif name == "corner_a":
            if value <= 0 or value >= 180:
                raise ValueError("Corner cannot be less 0 than or equal to 180")
            super().__setattr__("corner_a", value)

            super().__setattr__("corner_b", 180 - value)

        elif name == "corner_b":
            super().__setattr__("corner_b", value)
            super().__setattr__("corner_a", 180 - value)

        else:
            super().__setattr__(name, value)




r = Romb(10, 60)



print(r.side_a)
print(r.corner_a)
print(r.corner_b)

