# есть «Рейтинг»- собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating=[8,8,8,6,6,6,4,4,4,4,1,1]

new_elem= int(input('Введите новый элемент рейтинга: '))
inserted=False
i=0
for elem in rating:
    if new_elem > elem:
        rating.insert(i,new_elem)
        inserted=True
        break
    i+=1
    if not inserted:
        rating.append(new_elem)

print (rating)
