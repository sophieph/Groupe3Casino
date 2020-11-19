from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import make_response
from flask import url_for
import requests
import json

app = Flask(__name__, static_url_path='/', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def mainpage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    