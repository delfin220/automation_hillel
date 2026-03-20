# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

text_input = input("Введите текст: ")

unique_symbols = len(set(text_input))

if unique_symbols > 10:
    print(True)
else:
    print(False)