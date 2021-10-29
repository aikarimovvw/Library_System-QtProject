def check_number(number):
    correct = []
    for _ in range(910, 920):
        correct.append(str(_))
    for _ in range(980, 990):
        correct.append(str(_))
    for _ in range(920, 940):
        correct.append(str(_))
    for _ in range(902, 907):
        correct.append(str(_))
    for _ in range(960, 970):
        correct.append(str(_))

    number = number.strip(' ')
    if number[:2] == '+7':
        number = number[2:]
    elif number[:1] == '8':
        number = number[1:]
    else:
        return 'неверный формат в номере'
    count = ''
    if '--' not in number:
        if '(' in number or ')' in number:
            for i in list(number):
                if i == '(' or i == ')':
                    count += i
            if len(count) == 2:
                if ('(' in count and ')' in count) and (count.index('(') < count.index(')')):
                    pass
                else:
                    return 'неверный формат в номере'
            elif len(count) != 2 and len(count) != 0:
                return 'неверный формат в номере'
        if number[-1] == '-':
            return 'неверный формат в номере'
        number = ''.join(list(filter(lambda x: x.isdigit(), list(number))))

        if len(number) != 10:
            return 'неверное количество цифр'

        if number[:3] in correct:
            number_out = '+7' + number
            return 'ок'
        else:
            return 'не определяется оператор сотовой связи'

    else:
        return 'неверный формат в номере'


def check_name(name):
    if any(map(str.isdigit, name)):
        return 'В имени присутствуют цифры'
    elif not ''.join(list(filter(lambda x: x != '.' and x != ' ' and x != '-', name))).isalpha():
        return 'недопустимый формат имени'
    elif len(name) == 0:
        return 'введите имя'
    else:
        return 'ок'


def check_pass(password):
    repetition = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    if len(password) < 9:
        return 'длина пароля меньше 9 символов'
    if password.islower() or password.isupper():
        return 'в пароле все символы одного регистра'
    if password.isalpha():
        return 'в пароле нет ни одной цифры'
    if password.isdigit():
        return 'пароль состоит из цифр'
    if not any(map(str.isdigit, password)):
        return 'в пароле нет ни одной цифры'

    for i in repetition:
        for j in range(len(i) - 2):
            if i[j: j + 3] in password.lower():
                return 'в пароле есть комбинация из 3 буквенных символов, стоящих рядом в строке клавиатуры'
    return 'ок'


def check_login(login):
    if len(login) < 7:
        return 'логин слишком короткий '
    if ' ' in login:
        return 'используется пробел'
    if login.isdigit():
        return 'все символы - цифры'
    if login.islower() or login.isupper():
        return 'в пароле все символы одного регистра'
    if not any(map(str.isdigit, login)):
        return 'нет цифр  в логине'
    return 'ок'
