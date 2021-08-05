from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tictactoe'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

CORS(app)
mysql = MySQL(app)

# This is an example of a current game
current_game = [['X', 'O', ''], ['', '', ''], ['', '', '']]


@app.route('/')
def index():
    return 'Tic-Tac-Toe API'


@app.route('/books')
def books():
    query = 'select id, name from book'
    cur = mysql.connection.cursor()
    cur.execute(query)
    all_books = cur.fetchall()
    return jsonify(all_books)


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
    new_book = request.json
    book_name = new_book['name']

    try:
        insert_query = f"INSERT INTO book(name) VALUES ('{book_name}')"

        cur = mysql.connection.cursor()
        cur.execute(insert_query)
        mysql.connection.commit()

        response_message = [True, 'Book added successfully']
        return jsonify(response_message)
    except Exception as e:
        response_message = [False, f'An error occurred while adding book: {e}']
        return jsonify(response_message)


@app.route('/api/games/recent/', methods=['GET'])
def recent_games():
    query = 'select id, winner, result, playedOn from games order by playedOn desc;'
    cur = mysql.connection.cursor()
    cur.execute(query)
    past_games = cur.fetchall()
    return jsonify(past_games)


@app.route('/api/games/current/', methods=['GET'])
def current_games():
    return jsonify(current_game)


if __name__ == '__main__':
    app.run()
