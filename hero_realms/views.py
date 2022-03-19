from hero_realms import app
from flask import render_template, request


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/deadmatch_setup_step1', methods=['POST', 'GET'])
def deadmatch_setup_step1():

    return render_template('deadmatch_setup_step1.html')


@app.route('/deadmatch_setup_step2', methods=['POST', 'GET'])
def deadmatch_setup_step2():
    if request.method == 'POST':

        players_number = request.form['players_number']
        players = int(players_number) + 1

        return render_template('deadmatch_setup_step2.html', players_number=players)


@app.route('/deadmatch_game', methods=['POST', 'GET'])
def deadmatch_game():
    players_name = []
    try:
        for i in range(1, 8):
            players_name.append(request.form[f'player{i}_name'])
    except KeyError:
        pass
    return render_template('deadmatch_game.html', players_name=players_name)
