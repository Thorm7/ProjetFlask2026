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