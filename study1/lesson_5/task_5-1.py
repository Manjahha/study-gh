#Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('text.txt', 'w') as file:
    line=input('input text :\n')
    while line:
        file.write(f'{line}\n')
        line=input('text :\n')