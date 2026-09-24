# CHANGELOG.md — Historique des Modifications

Toutes les modifications notables apportées à ce projet sont consignées dans ce document.
Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/) et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [0.1.0] — Initialisation du projet & Setup Git
**Date** : 2026-09-23

### Ajouté
- Fichiers de cadrage méthodologique et architectural (`AGENTS.md`, `PROJECT.md`, `CONSTRAINTS.md`, `ARCHITECTURE.md`, `DEFINITION_OF_DONE.md`, `STATUS.md`, `TASKS.md`).
- Fichier `.gitignore` adapté à Python/Django, Node/React et aux variables d'environnement secrètes.
- Fichier `COMMANDS_USE.md` répertoriant de façon didactique l'ensemble des commandes exécutées par le développeur.
- Initialisation du dépôt Git local et synchronisation réussie avec le dépôt distant GitHub (`logi_doc_pro/main`).
- Initialisation complète du Backend Django avec connexion native PostgreSQL (`logidocdb` / `logidocadmin`), support automatique des DLL Windows (`libpq.dll`) et exécution des migrations de base avec succès.
- Formalisation des rôles et règles de gestion des Modèles (`PROJECT.md`, `docs/business/user-roles.md`, `docs/business/business-rules.md`).
- Initialisation du Frontend React avec Vite 8, React 19, Tailwind CSS v3 (avec PostCSS/Autoprefixer). Page de statut de l'environnement opérationnelle sur `http://localhost:5173`.
- **Phase 0 (Setup & Architecture) : TERMINÉE ✅**

## [0.2.0] — Phase 1 : Authentification & Base de données (en cours)
**Date** : 2026-09-24

### Ajouté
- Création de la base `logi_doc_pro` (PostgreSQL 18, encodage UTF-8, `OWNER logi_doc_pro_user`).
- Résolution du blocage `UnicodeDecodeError` psycopg2 : la base référencée n'existait pas ; le message d'erreur cp1252 de libpq masquait la vraie cause. Diagnostiqué via `psql` / `pg_isready`.
- Migration `0001_initial` (app `users`, modèle `CustomUser` avec champ `role`) appliquée.
- Endpoints d'authentification fonctionnels : `POST /api/auth/register/`, `GET/PATCH /api/auth/me/`, `POST /api/auth/token/`, `POST /api/auth/token/refresh/`.

### En cours
- Correction de `users/tests.py` et passage des 5 tests unitaires.

## [Démarrage Phase 1] — Authentification & Modèles de Données
**Date** : 2026-09-23

### En cours
- `[TASK-002]` : Authentification JWT & CustomUser Django.

