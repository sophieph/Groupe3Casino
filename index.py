from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import make_response
from flask import url_for
import pandas as pd
import datetime
import requests
import json

app = Flask(__name__, static_url_path='/', 
            static_folder='web/static',
            template_folder='web/templates')

#Page d'accueil
@app.route('/')
def mainpage():
    return render_template('index.html')

# Cherche si le joueur a déjà joué
@app.route('/', methods=["POST"])
def player_infos():
    nom = request.form["nom"]
    
    response = make_response(redirect(url_for('jeu')))
    response.set_cookie('nom', nom)
    return response

@app.route('/jeu')
def jeu():
    nom = request.cookies.get('nom')

    df = pd.read_csv('stat.csv')
    # df['date'] = df['date'].apply(lambda v: datetime.datetime.strptime(v, '%m/%d/%Y %H:%M:%S'))
    # latest_date =  df['date'].max()
    for row in df:
        if nom == row[2]:
            r = row
    return render_template('jeu.html', nom=nom, r=r)

if __name__ == "__main__":
    app.run(debug=True)