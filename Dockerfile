# Utiliser Python 3.14
FROM python:3.14

# Créer le dossier /app dans le container
WORKDIR /app

# Copier le fichier requirements.txt vers le container
COPY requirements.txt .

# Installer les bibliothèques
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet vers /app
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]