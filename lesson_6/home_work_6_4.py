# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for i in numbers:
    if i % 2 == 0:
        total = total + i
print(total)