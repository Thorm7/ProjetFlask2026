#__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Chemin absolu vers le dossier templates à la racine
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Clé secrète
app.config['SECRET_KEY'] = '03f4d5a0b4d45b85488d9b44f8f025eb'

# Supprime les notifications inutiles
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import urllib.parse
pwd = urllib.parse.quote_plus('admin')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{pwd}@localhost:5432/LivreDVD?client_encoding=utf8'
db = SQLAlchemy(app)

from app import routes