from hero_realms import app
from flask import url_for, render_template, request, redirect
from hero_realms.player import Player


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/deadmatch_setup_step1', methods=['POST', 'GET'])
def deadmatch_setup_step1():
    if request.method == 'POST':
        players_number = request.form['players_number']
        players = int(players_number) + 1
        return redirect(url_for('deadmatch_setup_step2', players_number=players))

    return render_template('deadmatch_setup_step1.html')


@app.route('/deadmatch_setup_step2', defaults={'players_number': 3}, methods=['POST', 'GET'])
@app.route('/deadmatch_setup_step2/<int:players_number>', methods=['POST', 'GET'])
def deadmatch_setup_step2(players_number):
    if request.method == 'POST':
        players = {}
        for i in range(1, 8):
            if request.form.get(f'player{i}_name'):
                players[f'Player{i}'] = Player(request.form.get(f'player{i}_name'))

        game(players)

    return render_template('deadmatch_setup_step2.html', players_number=players_number)


def game(players):
    while True:
        for player in players:
            print("Now is " + str(players[player]) + " turn")
            while True:
                end = input('Wanna end your turn?')
                if end.lower() == 'yes' or end.lower() == 'y':
                    print(str(players[player]) + " turn ended.")
                    break
