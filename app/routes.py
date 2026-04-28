from flask import render_template, request, redirect, url_for, flash
from . import app
from .models import Produit, Utilisateur
from flask_login import login_user, logout_user, login_required, current_user


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

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        utilisateur = Utilisateur.query.filter_by(email=email).first()
        # Comparaison directe sans bcrypt
        if utilisateur and utilisateur.mot_de_passe == mot_de_passe:
            login_user(utilisateur)
            print("Connecté")
            flash('Connecté avec succès', 'success')
            return redirect(url_for('accueil'))
        else:
            flash('Email ou mot de passe incorrect', 'danger')
    return render_template('connexion.html', title='Connexion')
@app.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    flash('Déconnecté', 'info')
    return redirect(url_for('accueil'))