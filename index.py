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

@app.route('/dashboard/<name>')
def dashboard_description(name):
    data_df = pd.read_csv('stat.csv')
    name_df = data_df[data_df.nom == name]

    min = name_df['niveau'].min()
    max = name_df['niveau'].max() 
    mise_moyenne = name_df['mise'].mean() 
    avg_nb_coup_lvl_1 = name_df[name_df['niveau'] == 1]['nb_coup'].mean()
    avg_nb_coup_lvl_2 = name_df[name_df['niveau'] == 2]['nb_coup'].mean()
    avg_nb_coup_lvl_3 = name_df[name_df['niveau'] == 3]['nb_coup'].mean()
    avgCoupArray = []
    avgCoupArray.insert(1,avg_nb_coup_lvl_1)
    avgCoupArray.insert(2,avg_nb_coup_lvl_2)
    avgCoupArray.insert(3,avg_nb_coup_lvl_3)

    return render_template('dashboard-description.html', name=name,
     min=min, max=max, mise_avg=mise_moyenne, avgCoupArray=avgCoupArray)

@app.route('/victory-avg/<name>', methods=['POST'])
def victory_avg_by_name(name):
    data_df = pd.read_csv('stat.csv')
    name_df = data_df[data_df.nom == name]
    victory = name_df['perdu'].value_counts(normalize=True)
    victoryArray = []
    for v in victory:
        victoryArray.append(v)
    
    return json.dumps({'victory':victoryArray})

@app.route('/victory/1/<name>', methods=['POST'])
def victory_lvl1_by_name(name):
    data_df = pd.read_csv('stat.csv')
    name_df = data_df[data_df.nom == name]

    victory = name_df[name_df['niveau'] == 1]['perdu'].value_counts(normalize=True)
    victoryArray = []
    for v in victory:
        victoryArray.append(v)
    
    return json.dumps({'victory':victoryArray})

@app.route('/victory/2/<name>', methods=['POST'])
def victory_lvl2_by_name(name):
    data_df = pd.read_csv('stat.csv')
    name_df = data_df[data_df.nom == name]
    victory = name_df[name_df['niveau'] == 2]['perdu'].value_counts(normalize=True)
    victoryArray = []
    for v in victory:
        victoryArray.append(v)
    
    return json.dumps({'victory':victoryArray})

@app.route('/victory/3/<name>', methods=['POST'])
def victory_lvl3_by_name(name):
    data_df = pd.read_csv('stat.csv')
    name_df = data_df[data_df.nom == name]
    victory = name_df[name_df['niveau'] == 3]['perdu'].value_counts(normalize=True)
    victoryArray = []
    for v in victory:
        victoryArray.append(v)
    
    return json.dumps({'victory':victoryArray})        

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

@app.route('/victory-avg', methods=['POST'])
def victory_avg():
    data_df = pd.read_csv('stat.csv')
    perdu = data_df['perdu'].astype('int64')
    victory = perdu.value_counts(normalize=True)
    victoryArray = []
    for v in victory:
        victoryArray.append(v)
    return json.dumps({'victory':victoryArray})

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