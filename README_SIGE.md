# 🏢 SIGE — Système Intégré de Gestion des Employés

> **Application web de gestion RH développée avec Django 6.0**  
> Centralisez, gérez et analysez les données de vos collaborateurs via une interface moderne, intuitive et responsive.

[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![DaisyUI](https://img.shields.io/badge/DaisyUI-5A0EF8?style=for-the-badge&logo=daisyui&logoColor=white)](https://daisyui.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Actif-28a745?style=for-the-badge)](https://github.com/)

---

## 📖 Description

**SIGE** (Système Intégré de Gestion des Employés) est une application web robuste développée avec le framework **Django 6.0**. Contrairement à une gestion sur tableur, elle centralise les données du personnel dans une **base de données relationnelle**, garantissant l'intégrité et la persistance des informations à long terme.

L'application couvre le **cycle de vie complet des données employés** via des opérations CRUD sécurisées, avec une interface professionnelle construite sur Tailwind CSS et DaisyUI (thème *Aqua*).

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| 📋 **Liste dynamique** | Affichage de tous les collaborateurs sous forme de cartes avec badges de statut |
| ➕ **Création** | Formulaire sécurisé avec validation via `ModelForm` |
| ✏️ **Modification** | Mise à jour fluide avec préremplissage automatique des champs |
| 🗑️ **Suppression** | Système de confirmation pour prévenir les pertes accidentelles |
| 📱 **Responsive Design** | Interface adaptée ordinateurs, tablettes et mobiles |
| 🎨 **Thème Aqua** | UI professionnelle et reposante via DaisyUI |
| 🔒 **Validation des données** | Contrôle d'intégrité à la saisie via `ModelForm` Django |

---

## 🛠️ Stack Technique

```
SIGE
├── Backend        → Python 3.14+ / Django 6.0.2
├── Frontend       → HTML5 / Tailwind CSS / DaisyUI (thème Aqua)
├── Architecture   → MVT (Modèle-Vue-Template)
├── Base de données→ SQLite (développement)
└── Formulaires    → Django ModelForm
```

| Couche | Technologie | Rôle |
|---|---|---|
| **Backend** | Python 3.14 + Django 6.0 | Logique métier, routing, ORM |
| **Frontend** | Tailwind CSS + DaisyUI | Stylisage responsive & composants UI |
| **Architecture** | MVT | Séparation des responsabilités |
| **Base de données** | SQLite | Persistance des données (dev) |
| **Templates** | Jinja2 / Django Templates | Rendu dynamique des vues |

---

## 🧱 Architecture MVT

```
┌──────────────────────────────────────────────────┐
│                   Navigateur                     │
│           (Requête HTTP / Réponse HTML)           │
└─────────────────────┬────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────┐
│                  urls.py                         │
│           (Routage des requêtes)                 │
└─────────────────────┬────────────────────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌─────────────────┐     ┌─────────────────────────┐
│    Views        │────▶│    Templates (.html)     │
│  (Logique       │     │  base.html + héritage    │
│   métier)       │     │  Tailwind CSS + DaisyUI  │
└────────┬────────┘     └─────────────────────────┘
         │
         ▼
┌─────────────────┐
│    Models       │
│  (Employe)      │
│  ORM Django     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    SQLite DB    │
│  (db.sqlite3)   │
└─────────────────┘
```

---

## 🗄️ Modélisation des Données

### Modèle `Employe`

```python
class Employe(models.Model):
    nom     = models.CharField(max_length=100)   # Nom complet
    email   = models.EmailField(unique=True)      # Email unique
    poste   = models.CharField(max_length=100)   # Intitulé du poste
    salaire = models.DecimalField(
                  max_digits=10,
                  decimal_places=2               # Rémunération en décimales
              )

    def __str__(self):
        return f"{self.nom} — {self.poste}"
```

| Champ | Type Django | Contrainte | Description |
|---|---|---|---|
| `nom` | `CharField` | max 100 caractères | Nom complet de l'employé |
| `email` | `EmailField` | `unique=True` | Adresse email unique |
| `poste` | `CharField` | max 100 caractères | Fonction / intitulé du poste |
| `salaire` | `DecimalField` | 10 chiffres, 2 décimales | Rémunération mensuelle |

---

## 🚀 Installation & Lancement

### Prérequis

- Python 3.14+
- pip
- virtualenv *(recommandé)*

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/sige-django.git
cd sige-django

# 2. Créer et activer l'environnement virtuel
python -m venv env
source env/bin/activate        # Linux / macOS
env\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 5. Créer un superutilisateur (accès admin)
python manage.py createsuperuser

# 6. Lancer le serveur de développement
python manage.py runserver
```

### Accès

| Interface | URL |
|---|---|
| Application principale | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) |
| Interface d'administration | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) |

---

## 📁 Structure du Projet

```
sige-django/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── sige/                        # Configuration principale Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── employe/                     # Application principale
    ├── models.py                # Modèle Employe
    ├── views.py                 # Logique CRUD
    ├── urls.py                  # Routes de l'app
    ├── forms.py                 # ModelForm sécurisé
    ├── admin.py                 # Enregistrement admin
    │
    └── templates/
        └── employe/
            ├── base.html        # Template de base (héritage)
            ├── liste.html       # Liste des employés (cartes)
            ├── ajouter.html     # Formulaire d'ajout
            ├── modifier.html    # Formulaire de modification
            └── supprimer.html   # Page de confirmation
```

---

## 🎨 Design & Expérience Utilisateur

L'interface repose sur le système d'**héritage de templates Django**, garantissant une cohérence visuelle sur toutes les pages :

```html
{% extends "employe/base.html" %}

{% block content %}
  <!-- Contenu dynamique injecté ici -->
{% endblock %}
```

**Choix de design :**
- Thème **Aqua** de DaisyUI → esthétique professionnelle et reposante
- Composants **cards** pour la liste des employés → lecture claire et rapide
- **Badges de statut** visuels pour identifier les postes en un coup d'œil
- Design **mobile-first** via Tailwind CSS

---

## 📊 Perspectives d'Évolution

La structure actuelle est conçue pour évoluer vers un **tableau de bord analytique** complet :

- [ ] 💰 Calcul automatique de la **masse salariale globale**
- [ ] 📊 Répartition des effectifs par **intitulé de poste** (graphique)
- [ ] 📈 Visualisation de données intégrée *(Chart.js / Plotly)*
- [ ] 🔐 Authentification utilisateur *(login / rôles)*
- [ ] 🐘 Migration vers **PostgreSQL** pour la production
- [ ] 📤 Export des données en **CSV / Excel**
- [ ] 🔔 Système de **notifications** internes

---

## 💡 Points Forts Techniques

### Architecture MVT rigoureuse
Séparation stricte entre la logique de données (**Models**), la logique métier (**Views**) et l'interface (**Templates**) — facilitant la maintenance et l'évolution du code.

### Sécurisation du CRUD
Toutes les opérations passent par Django `ModelForm`, qui assure la validation côté serveur et prévient les erreurs de saisie et les injections.

### Héritage de templates
Un unique fichier `base.html` centralise la charte graphique. Toutes les vues héritent de ce template, garantissant cohérence et non-répétition du code HTML.

### Interface Responsive
Tailwind CSS + DaisyUI offrent un rendu moderne s'adaptant aussi bien aux ordinateurs qu'aux tablettes et mobiles.

---

## 👤 Auteur

**Ngollo Wilson Miguel**  
Étudiant en ingénierie | Passionné de Data, Backend & Cloud  
🎯 Objectif : Analyste Business orienté AWS & Data

[![GitHub](https://img.shields.io/badge/GitHub-dj--wilson--pro-181717?style=flat-square&logo=github)](https://github.com/)

---

## 📄 Licence

Ce projet est réalisé dans un cadre éducatif et d'apprentissage du développement web avec Django.

---

<div align="center">
  <sub>Projet réalisé par Wilson Miguel — © 2026</sub>
</div>
