ima = input('Введите имя: ')
fam = input('Введите фамилию: ')
god = input('Введите год рождения: ')
gor = input('Введите город проживания: ')
email = input('Введите email: ')
tel = input('Введите телефон: ')


def personalinfo(ima, familia, godrozhdenia, gorod, email, tel):
    return str(f" {ima} {familia}, {godrozhdenia}г, гор. {gorod}, {email}, {tel}")


print(personalinfo(ima, fam, god, gor, email, tel))
