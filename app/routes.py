from flask import render_template, request
from . import app
from .models import Produit

@app.route('/')
@app.route("/accueil")
def accueil():
    # Récupérer toutes les catégories distinctes
    categories = Produit.query.with_entities(Produit.type_produit).distinct().all()
    return render_template('accueil.html',
                           title='Bienvenue dans notre boutique',
                           liste_cat=categories)

@app.route('/produits')
def produits():
    liste_produits = Produit.query.all()
    return render_template('produits.html', title='Nos produits', liste_prod=liste_produits)

@app.route('/produits_categorie')
def produits_categorie():
    type_produit = request.args.get('type_produit')
    liste_produits = Produit.query.filter_by(type_produit=type_produit).all()
    return render_template('produits_categorie.html',
                           title=f'Produits - {type_produit}',
                           produits=liste_produits,
                           categorie=type_produit)