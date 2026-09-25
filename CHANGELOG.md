# CHANGELOG.md — Historique des Modifications

Toutes les modifications notables apportées à ce projet sont consignées dans ce document. Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/) et le projet cherche à suivre [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### Modifié

- Audit de l'état réel du backend, du frontend, des tests, de l'architecture et de la documentation.
- Réalignement de `STATUS.md`, `TASKS.md`, `ROADMAP.md`, `REQUIREMENTS.md` et `ARCHITECTURE.md` sur le code présent.
- Distinction explicite entre fonctionnalité implémentée, implémentation partielle et résultat d'exécution non vérifié.
- Correction de la description du workflow `Template` et de la matrice RBAC.
- Remplacement du doublon de `DECISIONS.md` par un registre de décisions d'architecture.

### Ajouté

- Registre des problèmes connus et des risques dans `docs/ai/known-problems.md`.
- Documentation de prise en main du dépôt et du frontend.
- Matrice de traçabilité des exigences avec état d'avancement.

### Sécurité et confidentialité

- Aucun fichier `.env` ou `.env.*` n'a été ouvert, lu ou analysé pendant l'audit.
- Aucune valeur de secret, identifiant technique ou contenu d'environnement n'est ajoutée à la documentation.

## [0.2.0] — Authentification et fondations Documents

**Date** : 2026-09-24

### Ajouté

- Application Django `documents` avec les modèles `Template` et `Document`.
- Champs JSONB PostgreSQL pour la structure des modèles et le contenu des documents.
- Migration initiale `documents.0001_initial` dans le dépôt.
- Machine d'états de Template codée dans le modèle.
- Actions Django Admin de publication, rejet et archivage.
- Dix tests de modèles ajoutés dans `documents/tests.py`.
- Cinq tests d'authentification présents dans `users/tests.py`.
- Rotation des refresh tokens configurée dans SimpleJWT.

### Supprimé

- `COMMANDS_USE.md` a été retiré du suivi Git le 2026-09-23 ; le fichier présent localement est ignoré par `.gitignore`.

### État vérifié lors de cet audit

- Les routes `register`, `me`, `token` et `token/refresh` sont présentes dans le code.
- Les 15 tests backend sont écrits mais n'ont pas été exécutés pendant l'audit.
- Le résultat actuel de la base PostgreSQL et des migrations n'a pas été revérifié.
- Le logout avec blacklist, le RBAC cohérent, l'API Templates/Documents et l'intégration IA restent absents ou incomplets.

## [0.1.0] — Initialisation du projet et setup Git

**Date** : 2026-09-23

### Ajouté

- Documents de cadrage méthodologique et architectural (`AGENTS.md`, `PROJECT.md`, `CONSTRAINTS.md`, `ARCHITECTURE.md`, `DEFINITION_OF_DONE.md`, `STATUS.md`, `TASKS.md`).
- Fichier `.gitignore` destiné à exclure les fichiers d'environnement et secrets.
- Registre didactique `COMMANDS_USE.md`.
- Initialisation du dépôt Git et du backend Django avec PostgreSQL.
- Formalisation des rôles et des règles de gestion des modèles.
- Initialisation du scaffold frontend React avec Vite et Tailwind CSS.
- Phase 0 déclarée terminée.

### Réserves

- L'interface frontend de cette version est un placeholder et n'est pas considérée comme fonctionnelle.
- Les affirmations antérieures relatives à l'exécution des migrations, des endpoints et des tests doivent être revalidées avant d'être traitées comme des preuves actuelles.
