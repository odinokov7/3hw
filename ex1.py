

def razdel(arg1, arg2):
    if arg2 == 0:
        return str('Деление на 0')
    else:
        return arg1 / arg2


a = float(input('Введите 1-ое число: '))
b = float(input('Введите 2-ое число: '))

print(razdel(a, b))
