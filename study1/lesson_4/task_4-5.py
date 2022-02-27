#В список должны войти чётные числа от 100 до 1000 (включая границы).
#получить результат вычисления произведения всех элементов списка.

from functools import reduce

my_list = [i for i in range(100,1001) if i % 2 == 0]
sum = reduce((lambda x, y: x * y), my_list)

print(sum)
