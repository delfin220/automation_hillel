# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".


text_input = input("Enter a text: ")

while "h" not in text_input.lower():
    print(text_input)
    text_input = input("Enter a text: ")
