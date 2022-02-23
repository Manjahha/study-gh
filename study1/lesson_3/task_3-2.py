#функция принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func (name, surname, year, city, email, telephone):
    return f'{name}, {surname}, {year}, {city}, {email}, {telephone}'

a=input ('enter the name')
b=input('enter the surname')
c=input('enter the birth year')
d=input('enter the city')
e=input('enter the email')
f=input('enter the telephone number')

result=(my_func(name=a, surname=b, year=c, city=d, email=e, telephone=f))
print (result)
