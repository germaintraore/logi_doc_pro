# logi_doc_pro

Application web destinée à concevoir, personnaliser et générer des documents professionnels structurés, avec une future assistance IA et une modération des modèles.

## État actuel — 2026-09-25

Le dépôt est un **prototype précoce**, pas encore un MVP :

- backend Django/DRF configuré pour PostgreSQL ;
- authentification JWT partielle ;
- modèles `Template` et `Document` présents ;
- API Templates/Documents absente ;
- frontend React encore réduit à un placeholder ;
- CSS frontend actuellement invalide ;
- tests backend présents mais non exécutés lors du dernier audit ;
- aucun service IA ni déploiement de production.

Les détails et preuves figurent dans `STATUS.md`. Les problèmes ouverts sont recensés dans `docs/ai/known-problems.md`.

## Stack

- **Backend** : Python 3.10+, Django 5.1, Django REST Framework, SimpleJWT.
- **Base de données** : PostgreSQL exclusivement.
- **Frontend** : React 19, Vite 8, Tailwind CSS 3.
- **IA** : fournisseur à décider ; les appels LLM devront rester côté backend.

## Prérequis

- Python 3.10 ou supérieur.
- PostgreSQL accessible et configuré pour le backend.
- Node.js compatible avec Vite 8, notamment `^20.19.0` ou `>=22.12.0`.
- npm.

## Installation backend

Les commandes suivantes sont destinées au développeur local. L'IA ne doit jamais ouvrir, lire ou analyser les fichiers `.env` ou `.env.*` ; la préparation de la configuration secrète reste une responsabilité humaine.

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

L'adresse de développement attendue est généralement `http://127.0.0.1:8000/`, sous réserve de la configuration locale. L'API d'authentification commence sous `/api/auth/`.

## Installation frontend

```powershell
cd frontend
npm install
npm run dev
```

Le serveur Vite est généralement disponible sur `http://127.0.0.1:5173/`.

### Vérifications disponibles

```powershell
npm run lint
npm run build
```

ESLint passait lors du dernier audit, mais le build reste bloqué par l'erreur de syntaxe de `src/index.css`. Il ne faut donc pas considérer le frontend comme livrable avant correction et nouveau build.

## Structure du dépôt

```text
backend/              Django, API, modèles, migrations et tests
frontend/             React/Vite et styles
docs/                 Documentation métier, technique et workflow IA
tests/                Instructions de test transverses
PROJECT.md            Vision produit
REQUIREMENTS.md       Exigences traçables
ARCHITECTURE.md       Architecture cible et état réel
STATUS.md             État d'avancement
TASKS.md              Tâches opérationnelles
ROADMAP.md            Roadmap par phases
DECISIONS.md          Décisions d'architecture
CHANGELOG.md          Historique des changements
```

## Documents importants

- [Contraintes](CONSTRAINTS.md)
- [Définition de fin](DEFINITION_OF_DONE.md)
- [Règles métier](docs/business/business-rules.md)
- [Rôles et permissions](docs/business/user-roles.md)
- [Workflow IA](docs/ai/ai-workflow.md)
- [Problèmes connus](docs/ai/known-problems.md)
- [Frontend](frontend/README.md)

## Prochaines étapes prioritaires

1. Corriger le CSS frontend et valider le build.
2. Durcir la configuration Django et l'authentification JWT.
3. Trancher la source de vérité des droits administrateur.
4. Construire l'API Templates/Documents avec isolation des données.
5. Ajouter l'instanciation depuis un modèle publié et l'éditeur de documents.
6. Introduire l'IA uniquement après sécurisation du cœur métier.

## Confidentialité

Les secrets, JWT, mots de passe et valeurs d'environnement ne doivent jamais être placés dans la documentation, les logs ou les messages destinés à l'IA. Un fichier `.env` ne doit pas être ouvert pour résoudre une question d'audit ; demander au développeur de confirmer manuellement les prérequis nécessaires.
