from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from enum import Enum

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'gt122LEX152'
app.config['MYSQL_DB'] = 'tictactoe'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

CORS(app)
mysql = MySQL(app)

# This is an example of a current game
current_game = [['X', 'O', ''], ['', '', ''], ['', '', '']]


class BookStatus(Enum):
    Active = 1
    Deleted = 2
    Borrowed = 3


@app.route('/')
def index():
    return 'Tic-Tac-Toe API'


@app.route('/books')
def books():
    query = 'select id, book_name, BookStatus from books'
    cur = mysql.connection.cursor()
    cur.execute(query)
    all_books = cur.fetchall()
    for book in all_books:
        book_status = BookStatus(book['BookStatus'])
        book["BookStatus"] = book_status.name
    return jsonify(all_books)


@app.route('/deletedBooks')
def delete_books():
    deleted_book_status = BookStatus.Deleted
    query = f'select id, book_name, BookStatus from books where BookStatus={deleted_book_status.value}'
    cur = mysql.connection.cursor()
    cur.execute(query)
    all_books = cur.fetchall()
    for book in all_books:
        book_status = BookStatus(book['BookStatus'])
        book["BookStatus"] = book_status.name
    return jsonify(all_books)


@app.route('/borrowedBooks')
def borrow_books():
    borrowed_book_status = BookStatus.Borrowed
    query = f'select id, book_name, BookStatus from books where BookStatus={borrowed_book_status.value}'
    cur = mysql.connection.cursor()
    cur.execute(query)
    all_books = cur.fetchall()
    for book in all_books:
        book_status = BookStatus(book['BookStatus'])
        book["BookStatus"] = book_status.name
    return jsonify(all_books)


@app.route('/activeBooks')
def active_books():
    active_book_status = BookStatus.Active
    query = f'select id, book_name, BookStatus from books where BookStatus={active_book_status.value}'
    cur = mysql.connection.cursor()
    cur.execute(query)
    all_books = cur.fetchall()
    for book in all_books:
        book_status = BookStatus(book['BookStatus'])
        book["BookStatus"] = book_status.name
    return jsonify(all_books)


@app.route('/students')
def students():
    query = 'select id, student_name, gender from students'
    cur = mysql.connection.cursor()
    cur.execute(query)
    all_students = cur.fetchall()
    return jsonify(all_students)


@app.route('/players')
def players():
    query = 'select id, first_name, last_name from users'
    cur = mysql.connection.cursor()
    cur.execute(query)
    all_players = cur.fetchall()
    return jsonify(all_players)


@app.route('/book')
def get_book():
    book_id = request.args.get('id')
    if book_id is None:
        return jsonify('No book Id provided')

    query = f'select id, name from book where id={book_id}'
    cur = mysql.connection.cursor()
    cur.execute(query)
    book = cur.fetchone()
    if book is not None and len(book) > 0:
        return jsonify(book)
    return jsonify('No book found with that Id')


@app.route('/addbook', methods=['POST'])
def sign_up():
    # cur = mysql.connection.cursor()
    new_book = request.json
    print(new_book)
    # book_id = new_book(['id'])
    book_name = new_book['book_name']
    author = new_book['book_author']

    try:
        cur = mysql.connection.cursor()
        insert_query = f"INSERT INTO books(book_name,book_author) VALUES ('{book_name}', '{author}')"
        print(insert_query)

        cur.execute(insert_query)
        mysql.connection.commit()

        response_message = [True, 'Book added successfully']
        return jsonify(response_message)
    except Exception as e:
        response_message = [False, f'An error occurred while adding book: {e}']
        return jsonify(response_message)


@app.route('/addstudent', methods=['POST'])
def add_student():
    new_student = request.json
    print(new_student)
    student_name = new_student['student_name']
    gender = new_student['gender']

    try:
        cur = mysql.connection.cursor()
        insert_query = f"INSERT INTO students(student_name,gender) VALUES ('{student_name}', '{gender}')"
        print(insert_query)

        cur.execute(insert_query)
        mysql.connection.commit()

        response_message = [True, 'Student added ']
        return jsonify(response_message)
    except Exception as e:
        response_message = [False, f'An error occurred {e}']
        return jsonify(response_message)


@app.route('/addplayer', methods=['POST'])
def add_player():
    new_player = request.json
    print(new_player)
    first_name = new_player['first_name']
    second_name = new_player['second_name']
    games_played = new_player['games_played']

    try:
        cur = mysql.connection.cursor()
        insert_query = f"INSERT INTO users(first_name,last_name, games_played) VALUES ('{first_name}', '{second_name}','{games_played}')"
        print(insert_query)

        cur.execute(insert_query)
        mysql.connection.commit()

        response_message = [True, 'Player added ']
        return jsonify(response_message)
    except Exception as e:
        response_message = [False, f'An error occurred in adding player {e}']
        return jsonify(response_message)


@app.route('/deletestudent', methods=['DELETE'])
def delete_student():
    new_values = request.json
    print(new_values)
    student_id = new_values['id']

    try:
        cur = mysql.connection.cursor()
        delete_query = f"DELETE FROM students WHERE id = ('{student_id}')"
        print(delete_query)

        cur.execute(delete_query)
        mysql.connection.commit()

        response_message = [True, 'Student removed ']
        return jsonify(response_message)
    except Exception as e:
        response_message = [False, f'An error occurred in removing student {e}']
        return jsonify(response_message)


@app.route('/deletebook', methods=['DELETE'])
def delete_book():
    books = request.json
    print(books)
    book_id = books['id']
    query = f"SELECT id, book_name FROM books where id={book_id}"


@app.route('/api/games/recent/', methods=['GET'])
def recent_games():
    query = 'select id, winner_id, result, played_on from games order by played_on desc;'
    cur = mysql.connection.cursor()
    cur.execute(query)
    past_games = cur.fetchall()
    return jsonify(past_games)


@app.route('/api/games/current/', methods=['GET'])
def current_games():
    return jsonify(current_game)


if __name__ == '__main__':
    app.run()
