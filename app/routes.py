from flask import render_template
from . import app

@app.route('/')
@app.route("/accueil")
def accueil():
    return render_template('accueil.html', title='Bienvenue sur LibreDVD')

@app.route('/produits')
def produits():
    return render_template('produits.html', title='Nos produits')