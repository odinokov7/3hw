# Первый вариант. Функция принимает строку из нескольких слов.


a = str(input('Введите строку: '))
a = a.lower()


def int_func(arg):
    list_of_words = str(arg).split(' ')
    new_list = []
    result = ''
    for el in list_of_words:
        el = str(el)
        first_char = el[:1]
        first_char = first_char.upper()
        other_char = el[1:]
        obj = first_char + other_char
        new_list.append(obj)
    for el in new_list:
        result = result + ' ' + str(el)
    result = result[1:]  # Убираю пробел перед строчкой
    return result


print(int_func(a))

# Второй вариант. Функция принимает только одно слово.


def my_func(arg):
    arg = str(arg)
    first_char = arg[:1]
    first_char = first_char.upper()
    other_char = arg[1:]
    obj = first_char + other_char
    return obj


b = a
list_words = b.split(' ')
new_str = ''
for el in list_words:
    new_str = new_str + ' ' + my_func(el)
new_str = new_str[1:]  # Убираю пробел перед строчкой
print(new_str)
