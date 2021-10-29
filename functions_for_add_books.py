def check_title(name):
    if len(name) > 0:
        return 'ок'
    else:
        return 'Введите название, если его нет, то первую строку произведения'


def check_year(year):
    if (0 < int(year) < 2022) and year.isdigit():
        return 'ок'
    else:
        return 'Введите корректную дату публикации произведения'


def check_genre(genre):
    if len(genre) > 0:
        return 'ок'
    else:
        return 'Введите корректный жанр'
