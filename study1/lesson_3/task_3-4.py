#Программа принимает действительное положительное число x и целое отрицательное число y.
#возвести число x в степень y.
# Реализовать в виде функции my_func(x, y).
# При решении задания  обойтись без встроенной функции возведения числа в степень.

def my_func (x, y):
    result = x**y
    #result = 1/x**abs(y)
    return result

print(f'result {my_func(float(input("введите число положительное: ")), int(input("введите целое отрицательное число: ")))}')
