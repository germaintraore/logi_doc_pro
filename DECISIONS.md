# DECISIONS.md — Registre des Décisions d'Architecture

Ce document conserve les décisions structurées. La feuille de route produit se trouve dans `ROADMAP.md` et le détail des tâches dans `TASKS.md`.

## Statuts utilisés

- `CONFIRMÉ` : décision active du projet.
- `À DÉCIDER` : question ouverte qui doit être tranchée avant l'implémentation concernée.
- `À REVUE` : décision existante qui doit être réévaluée.

---

## ADR-001 — PostgreSQL comme base de données unique

- **Statut** : `CONFIRMÉ`
- **Contexte** : les documents sont structurés et doivent conserver les garanties relationnelles de Django.
- **Décision** : PostgreSQL est l'unique base de données. SQLite, MongoDB et Redis comme base principale sont interdits.
- **Conséquences** : les migrations, types JSONB, transactions et index sont conçus pour PostgreSQL ; l'environnement de test doit pouvoir créer une base dédiée.

## ADR-002 — Django REST Framework pour l'API

- **Statut** : `CONFIRMÉ`
- **Contexte** : le backend doit exposer une API JSON authentifiée et réutiliser l'ORM, l'administration et les permissions Django.
- **Décision** : utiliser Django et Django REST Framework avec l'authentification JWT par défaut.
- **Conséquences** : les serializers, permissions et querysets sont la frontière de validation et d'isolation ; les endpoints métier doivent être pensés DRF plutôt que comme des fonctions Django isolées.

## ADR-003 — React avec Vite et Tailwind CSS

- **Statut** : `CONFIRMÉ`
- **Contexte** : le produit nécessite une SPA moderne et une interface responsive.
- **Décision** : utiliser React avec composants fonctionnels, Vite comme outil de build et Tailwind CSS pour le style.
- **Conséquences** : les appels API doivent être centralisés dans `src/services/` ; la logique métier React doit être isolée des composants d'affichage selon `frontend/AGENTS.md`.

## ADR-004 — JWT avec rotation et blacklist

- **Statut** : `CONFIRMÉ` — décision active dont l'implémentation est incomplète.
- **Contexte** : l'authentification doit survivre au rechargement sans session serveur pour l'API.
- **Décision** : utiliser SimpleJWT avec access token court, refresh token plus long et rotation du refresh token.
- **Conséquences** : le frontend doit gérer le renouvellement et la déconnexion. L'endpoint de logout avec blacklist doit être ajouté avant de considérer le flux complet.

## ADR-005 — Contenu des documents en JSONB

- **Statut** : `CONFIRMÉ`
- **Contexte** : les structures de blocs sont flexibles et doivent être stockées dans PostgreSQL.
- **Décision** : utiliser les champs JSONB Django pour `Template.structure` et `Document.content`.
- **Conséquences** : la structure doit être validée par des serializers ou un schéma versionné. L'indexation n'est pas encore décidée : aucun index JSONB ne doit être déclaré comme existant tant qu'il n'est pas ajouté et justifié par les requêtes réelles.

## ADR-006 — Source de vérité des droits administrateur

- **Statut** : `À DÉCIDER`
- **Contexte** : le modèle possède `role`, `is_staff` et `is_superuser`, mais le workflow Template vérifie actuellement les deux derniers.
- **Décision** : aucune décision finale n'est prise dans cette mise à jour.
- **Conséquences** : tant que la décision n'est pas appliquée, un rôle `ADMIN` sans `is_staff` n'est pas administrateur effectif et un rôle `USER` avec `is_staff` peut obtenir des pouvoirs de modération. Une migration et des tests de non-régression seront nécessaires après décision.

## ADR-007 — Appels LLM exclusivement côté backend

- **Statut** : `CONFIRMÉ`
- **Contexte** : les secrets de fournisseur et les données de document ne doivent pas être exposés au navigateur.
- **Décision** : le frontend appellera uniquement des endpoints Django ; Django appellera le fournisseur LLM avec des règles de validation, de limitation et d'audit.
- **Conséquences** : le fournisseur, le modèle, la politique de conservation et le schéma des réponses restent à définir avant la Phase 4.

## ADR-008 — API Templates/Documents avant l'éditeur frontend

- **Statut** : `CONFIRMÉ`
- **Contexte** : construire l'interface avant les invariants métier produirait un frontend dépendant d'un contrat incomplet.
- **Décision** : sécuriser l'authentification et exposer les API Templates/Documents avec permissions et transactions avant le parcours d'édition complet.
- **Conséquences** : la roadmap réordonne le travail afin de réduire le risque de réécriture et de fuite de données.

---

## Points ouverts à trancher

- Source de vérité administrative : `role`, `is_staff`, `is_superuser` ou permission dédiée.
- Stratégie de stockage frontend des tokens.
- Schéma de version des blocs et compatibilité des documents existants.
- Indexation JSONB et requêtes de recherche prévues.
- Format d'export PDF/Word.
- Infrastructure de déploiement, sauvegardes et monitoring.
- Fournisseur et modèle LLM, limites de débit, politique de conservation des données et schéma des réponses.
