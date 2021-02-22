from hero_realms import app
from flask import url_for, render_template


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', title='Home')


@app.route('/deadmatch_setup_step1')
def deadmatch_setup_step1():
    return render_template('deadmatch_setup_step1.html')
