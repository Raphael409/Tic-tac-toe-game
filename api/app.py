from flask import Flask, jsonify

app = Flask(__name__)

#  This is  an example of saved games
past_games = [
    {
        'when': '2020-08-06',
        'winner': 'X'
    },
    {
        'when': '2020-08-05',
        'winner': 'O'
    },
    {
        'when': '2020-08-04',
        'winner': 'X'
    },
    {
        'when': '2020-08-02',
        'winner': ')'
    }
]
# This is an example of a current game
current_game = [['X', 'O', ''], ['', '', ''], ['', '', '']]


@app.route('/')
def index():
    return 'Tic-Tac-Toe API'


@app.route('/api/games/recent/', methods=['GET'])
def recent_games():
    return jsonify(past_games)


@app.route('/api/games/current/', methods=['GET'])
def current_games():
    return jsonify(current_game)


if __name__ == '__main__':
    app.run()
