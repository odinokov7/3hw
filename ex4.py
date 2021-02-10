x = float(input('Введите x: '))
y = int(input('Введите y: '))
if y == 0:
    print('y не может быть 0')
elif y > 0:
    y = y * -1


def my_func_first_try(arg1, arg2):
    return arg1 ** arg2


def my_func_second_try(arg1, arg2):
    arg2 = abs(arg2)
    otv = arg1
    for i in range(1, arg2):
        otv = otv * arg1
        i += 1
    return 1 / otv


print(my_func_first_try(x, y))
print(my_func_second_try(x, y))
