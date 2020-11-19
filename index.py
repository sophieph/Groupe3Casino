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

@app.route('/jeu')
def jeu():
    nom = request.cookies.get('nom')

    value = ''
    with open("stat.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if nom == row[2]:
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