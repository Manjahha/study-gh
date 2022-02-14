#Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number=int(input('введите целое положительное число: '))
i=number%10
number=number//10
while number>0:
    if number%10>i:
        i=number%10
    number=number//10
print (i)
