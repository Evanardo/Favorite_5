from app import app
from flask import render_template
from flask import url_for

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/band')
def band():
    return render_template('band.html')

@app.route('/decade')
def decade():
    return render_template('decade.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/tw')
def tw():
    return render_template('time_waster.html')