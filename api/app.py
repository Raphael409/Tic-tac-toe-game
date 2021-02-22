from flask import Flask, jsonify
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
