# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

file_name, worked_hour, rate, bonus = argv

calculation = ((float(worked_hour) * float(rate)) + float(bonus))
print(f'common {calculation}')
