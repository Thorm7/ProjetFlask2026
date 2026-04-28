from app import db

class Produit(db.Model):
    __tablename__ = 'produit'  # Nom de la table en base de données

    id_produit = db.Column(db.Integer, primary_key=True)
    nom_produit = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    prix = db.Column(db.Numeric(8, 2))  # Pour les prix (ex: 12.99)
    stock = db.Column(db.Integer)
    image_url = db.Column(db.String(255))      # Champ pour l'URL de l'image
    type_produit = db.Column(db.String(100))   # Champ pour la catégorie

    def __repr__(self):
        return f'<Produit {self.nom_produit}>'

from flask_login import UserMixin

class Utilisateur(db.Model, UserMixin):
    __tablename__ = 'utilisateur'

    id_user = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    role = db.Column(db.String(50), default='user')

    def get_id(self):
        return str(self.id_user)