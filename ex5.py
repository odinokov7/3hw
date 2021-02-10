# ` - для завершения программы
# Данная програма ищет только цифры и игнорирует другие символы
summa = 0
n = 0
while 1 > n:
    stroka = str(input('Введите числа через пробел: '))
    list_of_char = stroka.split(' ')
    for el in list_of_char:
        if el == '`':
            n += 1
            break
        if el.isnumeric():
            summa = summa + int(el)
    print('Сумма равна:', summa)


