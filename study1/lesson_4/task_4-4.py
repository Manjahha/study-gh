#в списке пределите элементы без повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

my_list = [4, 5, 42, 4, 5, 7, 23, 1, 43, 43, 3, 5, 10, 7, 4, 1]
new_list = [i for i in my_list if my_list.count(i) == 1]

print(new_list)
