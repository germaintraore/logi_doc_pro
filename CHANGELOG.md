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
