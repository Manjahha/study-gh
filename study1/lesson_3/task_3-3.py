# my_func(), принимает три позиционных аргумента,
# возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg1>=arg2 and arg2>=arg3:
       return arg1+arg2
    elif arg1>=arg2 and arg2<=arg3:
        return arg1+arg3
    else:
        return arg2+arg3

print(f'result - {my_func(int(input("enter the number: ")), int(input("enter the number: ")), int(input("enter the number: ")))}')
