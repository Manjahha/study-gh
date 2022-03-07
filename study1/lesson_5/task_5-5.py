#Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

with open('text_5.txt', 'w') as file:
    for _ in range(30):
        file.write(f'{random.randint(0,10)}')

with open('text_5.txt') as file:
    nums=file.read().split()
    summ=0
    for n in nums:
        summ+= int(n)
print(summ)