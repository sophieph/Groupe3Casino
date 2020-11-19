from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import make_response
from flask import url_for
import pandas as pd
import numpy
from matplotlib import pyplot as plt
import datetime
import requests
import json
import csv

from Player import Player
from Niveau import Niveau
from Global import Global


app = Flask(__name__, static_url_path='/', 
            static_folder='web/static',
            template_folder='web/templates')

level = Niveau(1)
player = Player(level)
g = Global(player, level)


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

@app.route('/dashboard')
def dashboard():

    data_df = pd.read_csv('stat.csv')

    # Find unique player
    names = data_df["nom"].unique()

    #Average level reached
    levels = data_df['niveau'].value_counts(normalize=True)

    return render_template('dashboard.html', names=names, levels=levels)

@app.route('/levels-avg', methods=['POST'])
def levels_avg():
    data_df = pd.read_csv('stat.csv')
    levels = data_df['niveau'].value_counts(normalize=True)
    levelArray = []
    for l in levels:
        levelArray.append(l)
    return json.dumps({'levels':levelArray})

@app.route('/winnings-avg', methods=['POST'])
def winnings_avg():
    data_df = pd.read_csv('stat.csv')
    niveau_1 = data_df[data_df['niveau'] == 1]['gain'].mean()  
    niveau_2 = data_df[data_df['niveau'] == 2]['gain'].mean()  
    niveau_3 = data_df[data_df['niveau'] == 3]['gain'].mean()

    winningArray = []
    winningArray.append(niveau_1)
    winningArray.append(niveau_2)
    winningArray.append(niveau_3)
    
    return json.dumps({'winnings':winningArray})



@app.route('/jeu')
def jeu():
    nom = request.cookies.get('nom')

    value = ''
    with open("stat.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if nom == row[1]:
                value = row

    return render_template('jeu.html', nom=nom, value=value)

@app.route('/set-level', methods=['POST'])
def set_level():
    level =  int(request.form["level"])
    if level < 1 or level > 3:
        return json.dumps({'status':'error','level':level})
    else:
        global player
        player.set_level(Niveau(level))
        
        return json.dumps({'status':'OK','level':player.level.level, 'nb_python': player.level.nb_python})


if __name__ == "__main__":
    app.run(debug=True)