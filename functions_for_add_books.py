from datetime import date
from datetime import datetime

input_len = 0


def check_len(name):
    if len(name) != input_len:
        return True
    else:
        return False


def check_year(year):
    current_date = date.today()
    if year.isdigit() and int(year) <= current_date.year:
        return True
    return False


def check_date(b_date):
    b_date = datetime.strptime(b_date, "%Y-%m-%d")
    difference = datetime.today() - b_date
    if difference.days > 0:
        return True
    else:
        return False


def paste(item):
    if item == 'author':
        return """SELECT author from Authors WHERE author=? """
    else:
        return """SELECT genre from Genres WHERE genre=? """
