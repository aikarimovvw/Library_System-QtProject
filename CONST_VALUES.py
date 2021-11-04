INPUT_LEN = 0
DATE = 0
EMPLOYEE = 'Employee'
AUTHORS = 'Authors'
GENRES = 'Genres'
CLIENTS = 'clients'
BOOKS = 'Books'
OPERATIONS = 'Operations'
ID = 'id'
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
AVAILABLE_TRUE = 1
AVAILABLE_FALSE = 0

TABLES = {'Employee': ('id', 'password', 'name', 'number', 'login'),
          'Authors': ('id', 'author'),
          'Books': ('id', 'author_name', 'book', 'genre_name', 'path_image', 'description', 'year', 'available'),
          'Genres': ('id', 'genre'),
          'clients': ('id', 'client_name', 'client_number', 'client_mail', 'client_adres', 'client_date'),
          'Operations': ('id', 'book_name', 'book_id', 'type', 'from', 'to', 'client_name', 'client_id')}
