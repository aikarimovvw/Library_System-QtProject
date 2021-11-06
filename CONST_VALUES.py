INPUT_LEN = 0
ALL_VALUES = '*'
EMPLOYEE = 'Employee'
AUTHORS = 'Authors'
GENRES = 'Genres'
CLIENTS = 'clients'
BOOKS = 'Books'
OPERATIONS = 'Operations'
ID = 'id'
EMPTY_LINE = ''
PASSWORD = 'password'
NAME = 'name'
NUMBER = 'number'
LOGIN = 'login'
CLIENT_NUMBER = 'client_number'
BOOK = 'book'
AUTHOR_NAME = 'author_name'
AUTHOR = 'author'
GENRE = 'genre'
CLIENT_NAME = 'client_name'
BOOK_NAME = 'book_name'
AVAILABLE = 'available'
BOOK_ID = 'book_id'
AVAILABLE_TRUE = 1
AVAILABLE_FALSE = 0
RED_STATUS = "color : red"
GREEN_STATUS = "color : green"
FORMAT_YEAR = "%Y-%m-%d"
DATE_YMD = '"yyyy-MM-dd"'
DATE_DEADLINE = 'date_deadline'
CLIENT_ID = 'client_id'
FONT = 'Times'
REGISTRATION_WIND = 'Регистрация'
SUCCESSFULLY = 'Успешно'
WIND_AUTHORIZATION = 'Авторизация'
STYLE_PRESS = "WidgetItem:pressed"
CORRECT_DATE_PUB = 'Введите корректную дату публикации произведения'
LEN_ZERO = 'Пустая строка, введите заново'
ADD_BOOK_COMPLETE = 'Книга успешно добавлена!'
ADD_CLIENT_COMPLETE = 'Клиент успешно добавлен!'
CHOICE_AUTHOR = 'Выбор автора'
CHOICE_GENRE = 'Выбор жанра'
CHOICE = 'Выбор'
PUT_IMAGE = 'Выбрать картинку'
ADD_BOOK = 'Добавление книги'
MAIN_WINDOW = 'Главное окно'
GREAT_OPERATION = 'Операция успешно выполнена'
FORMAT_DB = 'QSQLITE'
WRONG_ID = 'Введите правильный id книги/читателя'
WROND_ID_BOOK = 'Введите корректное id'
AVAILABLE_IN_STOCK = 'Эта книга в библиотеке'
NOT_AVAILABLE_IN_STOCK = 'На данный момент книги нет в библиотеки'
MESS_NUM_ERROR = 'Такого номера нет, введите заново, либо создайте аккаунт'
MESS_CORRECT_NUM = 'Введите корректный номер'
CORRECT_B_DATE = 'Введите корректную дату рождения'
INCORRECT_USER = 'Такой пользователь уже существует'
INCORRECT_LOGIN = 'Введите корректный логин'
INCORRECT_PASSWORD = 'Неправильный пароль'
LOGIN_EXISTS = 'Пользователь с таким логином существует'
WIND_ADD_CLIENT = 'Добавление читателя'
INCORRECT_VALUES = 'Введите корректные данные'
INCORRECT_CLIENT = 'Клиент с таким номером существует'
DIFF_DAYS_CHECK_ZERO = 0
SHOW_DEBTORS = 'Отображение должников'
SHOW_INF = 'Отображение информации'
EXTRADITION = 'Выдача'
REFUND = 'Возврат'
AUTHOR_RUS = 'Автор'
DATA_IS_ENTERED = 'Данные занесены, можете продолжить вход'

GET_ZERO_ELEMENT = 0

# индексы для запросов к бд к разным таблицам
ZERO_VALUE = 0
FIRST_VALUE = 1
SECOND_VALUE = 2
THIRD_VALUE = 3
FOURTH_VALUE = 4
FIFTH_VALUE = 5
SIXTH_VALUE = 6
SEVENTH_VALUE = 7

# номера колонок в Table Widget
ZERO_COLUMN = 0
FIRST_COLUMN = 1
SEC_COLUMN = 2
THIRD_COLUMN = 3
FOURTH_COLUMN = 4

# Коннект Main Tab Widget c кнопками
ZERO_TAB = 0
FIRST_TAB = 1
SECOND_TAB = 2
THIRD_TAB = 3

TABLES = {'Employee': ('id', 'password', 'name', 'number', 'login'),
          'Authors': ('id', 'author'),
          'Books': ('id', 'author_name', 'book', 'genre_name', 'path_image', 'description', 'year', 'available'),
          'Genres': ('id', 'genre'),
          'clients': ('id', 'client_name', 'client_number', 'client_mail', 'client_adres', 'client_date'),
          'Operations': ('id', 'book_name', 'book_id', 'type', 'from', 'to', 'client_name', 'client_id')}
