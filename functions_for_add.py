from datetime import date
from datetime import datetime
from CONST_VALUES import *
import library_db


def check_len(name):
    if len(name) != INPUT_LEN:
        return True
    else:
        return False


def check_year(year):
    current_date = date.today()
    if year.isdigit() and int(year) <= current_date.year:
        return True
    return False


def check_date(b_date):
    b_date = datetime.strptime(b_date, FORMAT_YEAR)
    difference = datetime.today() - b_date
    if difference.days > 0:
        return True
    else:
        return False


def check_clients(name, num_client, mail_client, address_client, b_date):
    name_check = check_len(name)
    number_check = check_len(num_client)
    mail_check = check_len(mail_client)
    address_check = check_len(address_client)
    year_check = check_date(b_date)
    if all([name_check, number_check, mail_check, address_check]):
        if year_check is False:
            return False
        return True
    else:
        return False


def delete_operations():
    res_book = set(library_db.select_table(OPERATIONS, BOOK_NAME))
    for i, item in enumerate(res_book):
        res_available = library_db.select_one_with_aspect(BOOKS, BOOK, item[0], AVAILABLE)
        if res_available[0] == AVAILABLE_TRUE:
            library_db.delete_values(OPERATIONS, BOOK_NAME, item[0])


def check_employee(name_employee, number, password, login):
    login_check = check_len(login)
    pass_check = check_len(password)
    number_check = check_len(number)
    name_check = check_len(name_employee)

    if all([login_check, pass_check, number_check, name_check]):
        return True
    else:
        return False
