# Comptabilité API

Ce projet est une API de gestion comptable développée avec Django et Django REST Framework. Il permet de gérer des comptes comptables, d'enregistrer des transactions et de générer des rapports de balance comptable.

## Prérequis

- Python 3.10 ou supérieur
- PostgreSQL
- Node.js (si vous utilisez des outils front-end comme Electron)

## Installation

### 1. Cloner le dépôt

Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/g0sh5ukuna/comptabilite_app
cd Test
```

### 2. Configurer l'environnement virtuel

Créez et activez un environnement virtuel :

```bash
python -m venv testenv
source testenv/bin/activate  # Sur Windows, utilisez `testenv\Scripts\activate`
```

### 3. Installer les dépendances

Installez les dépendances Python listées dans requirements.txt :

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

Créez une base de données PostgreSQL et configurez-la dans le fichier `settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'comptabilite',
        'USER': 'db_admin_test',
        'PASSWORD': 'compt2@25Benin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Appliquer les migrations

Appliquez les migrations pour créer les tables de la base de données :

```bash
python manage.py migrate
```

### 6. Créer un superutilisateur

Créez un superutilisateur pour accéder à l'interface d'administration :

```bash
python manage.py createsuperuser
```

### 7. Démarrer le serveur

Lancez le serveur de développement :

```bash
python manage.py runserver
```

Accédez à l'application via [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Utilisation

### Interface d'administration

Accédez à l'interface d'administration via [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) et connectez-vous avec le superutilisateur que vous avez créé. Vous pouvez gérer les comptes comptables, les transactions et les entrées du journal via cette interface.

### API Endpoints

#### Comptes comptables : `/api/accounts/`

- `GET` : Lister les comptes
- `POST` : Créer un compte
- `GET /api/accounts/{id}/` : Détails d’un compte
- `PUT /api/accounts/{id}/` : Modifier un compte
- `DELETE /api/accounts/{id}/` : Supprimer un compte

#### Transactions : `/api/transactions/`

- `POST` : Enregistrer une transaction
- `GET` : Lister les transactions
- `GET /api/transactions/{id}/` : Voir le détail d’une transaction

#### Journal comptable : `/api/journal/`

- `GET` : Voir l’historique des écritures

#### Exporter la balance comptable : `/api/export-balance/export_balance/`

- `GET` : Générer un fichier Excel avec la balance comptable

## Contribuer

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commitez vos modifications (`git commit -m 'Ajouter une nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT.