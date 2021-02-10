a = float(input('Введите 1-ое число: '))
b = float(input('Введите 2-ое число: '))
c = float(input('Введите 3-ье число: '))


def my_func(var1, var2, var3):
    my_list = [var1, var2, var3]
    my_list.sort()
    return my_list[1] + my_list[2]


print(my_func(a, b, c))
