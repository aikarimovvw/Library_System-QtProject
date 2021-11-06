import sqlite3
from CONST_VALUES import *

con = sqlite3.connect('db_lib.sqlite')
cur = con.cursor()


def select_table(table_name, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name}"""
    return cur.execute(value).fetchall()


def select_one_with_aspect(table_name, field, field_value, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE {field}=?"""
    return cur.execute(value, (field_value,)).fetchone()


def select_all_with_aspect(table_name, field, field_value, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE {field}=?"""
    return cur.execute(value, (field_value,)).fetchall()


def insert_for_employee(*values):
    cur.execute("""INSERT INTO Employee(login, password, number, name)  
                                    VALUES(?, ?, ?, ?)""", values).fetchall()
    con.commit()


def insert_for_books(*values):
    cur.execute("""INSERT INTO Books(author_name, book, genre_name, description, year, path_image, availible) 
                    VALUES(?, ?, ?, ?, ?, ?, ?)""", values).fetchall()
    con.commit()


def insert_for_name(table_name, field, parameter):
    value = f"""INSERT INTO {table_name}({field}) VALUES(?)"""
    cur.execute(value, (parameter,)).fetchall()
    con.commit()


def insert_for_clients(*values):
    cur.execute("""INSERT INTO clients(client_name, client_number, client_mail, client_adres, client_date) 
                        VALUES(?, ?, ?, ?, ?)""", values)
    con.commit()


def delete_values(table_name, field, parameter):
    value = f"""DELETE from {table_name} WHERE {field}==?"""
    cur.execute(value, (parameter,))
    con.commit()


def select_with_like_operation(table_name, field, field_value, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE {field} LIKE ?"""
    return cur.execute(value, (field_value,)).fetchall()


def update_clients_values(values):
    cur.execute(
        """UPDATE clients SET client_name=?, client_number=?, client_mail=?, client_adres=?, client_date=? 
        WHERE id=? """, values)
    con.commit()


def update_books_values(values):
    cur.execute(
        """UPDATE Books SET author_name=?, book=?, genre_name=?, description=?, year=? WHERE id=? """, values)
    con.commit()


def update_employ_values(values):
    cur.execute(
        """UPDATE Employee SET password=?, name=?, number=?, login=? WHERE login=? """, values)
    con.commit()


def update_book_available(values):
    available = values[ZERO_VALUE]
    if available == AVAILABLE_TRUE:
        available = AVAILABLE_FALSE
        cur.execute(
            """UPDATE Books SET available=? WHERE id=? """, (available, values[FIRST_VALUE],))
    else:
        available = AVAILABLE_TRUE
        cur.execute(
            """UPDATE Books SET available=? WHERE id=? """, (available, values[FIRST_VALUE],))
    con.commit()


def insert_to_operations(*values):
    cur.execute("""INSERT INTO Operations(book_name, book_id, type, date_of_issue, date_deadline, client_name, client_id) 
                            VALUES(?, ?, ?, ?, ?, ?, ?)""", values)
    con.commit()
