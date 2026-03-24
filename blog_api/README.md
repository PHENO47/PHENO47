📰 Blog API Backend – Flask

📌 Description

Ce projet est une API backend développée avec Flask permettant de gérer un blog simple.
Elle offre des fonctionnalités complètes pour créer, lire, modifier, supprimer et rechercher des articles.

Ce projet a été réalisé dans le cadre du cours INF222 – Développement Backend.

---

🚀 Technologies utilisées

- Python 3
- Flask
- SQLite

---

📁 Structure du projet

blog_api/
│
├── app.py
├── config.py
│
├── models/
├── controllers/
├── routes/
├── database/
│
└── README.md

---

⚙️ Installation

1. Cloner le projet

git clone https://github.com/PHENO47/blog-api.git
cd blog-api

2. Installer les dépendances

pip install flask

3. Lancer le serveur

python app.py

Le serveur sera accessible à l’adresse :

http://127.0.0.1:5000

---

📡 Endpoints disponibles

🔹 Créer un article

- POST "/api/articles"

Body JSON :

{
  "titre": "Mon article",
  "contenu": "Contenu ici",
  "auteur": "Samuel",
  "categorie": "Tech",
  "tags": ["python", "api"]
}

---

🔹 Obtenir tous les articles

- GET "/api/articles"

---

🔹 Obtenir un article

- GET "/api/articles/{id}"

---

🔹 Modifier un article

- PUT "/api/articles/{id}"

---

🔹 Supprimer un article

- DELETE "/api/articles/{id}"

---

🔹 Rechercher un article

- GET "/api/articles/search?query=mot"

---

🧪 Tests

Les tests peuvent être effectués avec :

- Postman
- Navigateur web

---

📌 Bonnes pratiques appliquées

- Architecture MVC (Model - Controller - Routes)
- Validation des entrées
- Utilisation des codes HTTP standards
- Base de données SQLite

---

👨‍💻 Auteur

- Nom : NZAPA-AKE SAMUEL 
- Filière : Informatique
- UE : INF222

---

📚 Objectif pédagogique

Ce projet vise à comprendre :

- la création d’API REST
- la gestion des données avec SQLite
- la structuration d’un projet backend

---

🔥 Améliorations possibles

- Ajout d’une authentification (JWT)
- Documentation Swagger
- Déploiement en ligne
- Interface frontend

---
