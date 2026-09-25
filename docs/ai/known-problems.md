# Problèmes Connus et Risques

**Dernière revue** : 2026-09-25
**Périmètre** : dépôt `logi_doc_pro`, hors fichiers `.env`, `.env.*`, secrets et dépendances générées.

## Règle de confidentialité

L'audit ne doit jamais ouvrir, lire ou analyser un fichier `.env` ou `.env.*`. Les vérifications de secrets, de variables d'environnement et de privilèges PostgreSQL doivent être réalisées manuellement par le développeur, sans transmettre leurs valeurs.

## P0 — Bloquants de fond

### P0-001 — CSS frontend invalide

- **Constat** : `frontend/src/index.css` contient des blocs mal appariés et un `Unexpected }` détecté par l'analyse PostCSS.
- **Impact** : le build Vite ne peut pas être considéré comme valide ; l'interface n'est pas livrable.
- **Action** : corriger la structure, lancer le build, puis supprimer les styles de template inutilisés.

### P0-002 — Configuration Django non fail-closed

- **Constat** : `backend/config/settings.py` fournit une valeur de secours pour la clé Django et active `DEBUG` par défaut.
- **Impact** : un démarrage sans configuration valide peut exposer un comportement de développement en environnement partagé.
- **Action** : exiger les variables sensibles, interdire la valeur de secours en production et documenter les profils d'exécution.

### P0-003 — Autorisation administrative incohérente

- **Constat** : le rôle métier `role` n'est pas la source d'autorité utilisée par le workflow ; `is_staff` et `is_superuser` le sont.
- **Impact** : risque de mauvais refus d'accès ou d'escalade de privilèges.
- **Action** : décider la stratégie RBAC, la documenter, créer une migration si nécessaire et la couvrir par des tests.

## P1 — Bloquants fonctionnels et sécurité

### P1-001 — Logout JWT absent

- **Constat** : la rotation est configurée, mais aucun endpoint de logout ne blacklist le refresh token.
- **Impact** : un refresh token peut rester utilisable jusqu'à expiration après une déconnexion.
- **Action** : ajouter l'endpoint SimpleJWT de blacklist et tester l'impossibilité de réutilisation.

### P1-002 — API Templates/Documents absente

- **Constat** : aucun serializer, queryset, router ou endpoint métier n'est présent.
- **Impact** : aucun parcours de bout en bout n'est exposé par l'API pour le catalogue, la modération, l'instanciation et l'édition ; certaines transitions existent toutefois dans le modèle et Django Admin.
- **Action** : définir les contrats, permissions, filtres de propriété et erreurs avant de construire l'éditeur.

### P1-003 — Instanciation depuis un modèle publié non garantie

- **Constat** : aucun service ne vérifie `PUBLISHED` avant la création d'un Document.
- **Impact** : des documents invalides peuvent être créés depuis un brouillon ou un modèle archivé.
- **Action** : créer un service de factory transactionnel qui copie une structure validée.

### P1-004 — Workflow Django Admin incomplet

- **Constat** : `created_by` n'est pas initialisé de façon fiable, la publication officielle n'est pas distincte et les exceptions sont ignorées.
- **Impact** : modèles non conformes et faux messages de succès.
- **Action** : réécrire les actions avec transactions, autorisations explicites et propagation des erreurs.

### P1-005 — Validation de sécurité incomplète

- **Constat** : les validateurs Django ne sont pas appelés à la création, `is_active` est modifiable par le profil et aucun throttling DRF n'est configuré.
- **Impact** : mots de passe faibles, désactivation abusive et force brute possible.
- **Action** : traiter ces points dans TASK-002 et ajouter des tests de non-régression.

## P2 — Qualité et performance

### P2-001 — JSONB sans index

- **Constat** : `Template.structure` et `Document.content` sont JSONB, mais aucun index JSON n'est déclaré.
- **Impact** : l'indexation n'est pas encore définie ; des recherches JSON futures pourront être coûteuses si les mesures conduisent à ajouter une optimisation ciblée.
- **Action** : mesurer les requêtes réelles avant de choisir un index GIN ou un index d'expression.

### P2-002 — Schéma JSON non validé

- **Constat** : aucune validation de structure de blocs n'est appliquée.
- **Impact** : documents mal formés difficiles à migrer ou à afficher.
- **Action** : définir un schéma versionné et le valider dans les serializers et les services.

### P2-003 — Concurrence non maîtrisée

- **Constat** : pas de version optimiste, de `select_for_update` ou de journal de revue.
- **Impact** : lost updates et transitions concurrentes incohérentes.
- **Action** : ajouter un contrôle de concurrence et des tests de concurrence.

### P2-004 — Tests et CI absents ou incomplets

- **Constat** : 15 tests backend sont présents mais non exécutés pendant l'audit ; aucun test frontend ni workflow CI n'est présent.
- **Impact** : régressions détectées tard et statut de livraison peu fiable.
- **Action** : exécuter les tests, ajouter lint/typecheck selon les outils choisis et créer un pipeline minimal.

### P2-005 — Dépendances backend non verrouillées

- **Constat** : `backend/requirements.txt` contient des bornes minimales, sans fichier de verrouillage Python.
- **Impact** : installations potentiellement différentes selon la date.
- **Action** : définir une politique de verrouillage compatible avec le projet, sans ajouter de dépendance lourde.

## P3 — Produit et exploitation

### P3-001 — Frontend non fonctionnel

- **Constat** : React est un placeholder sans Router, client API, gestion de session ni pages métier.
- **Impact** : aucun parcours utilisateur n'est démontrable en dehors d'un écran de statut.
- **Action** : corriger le build avant toute fonctionnalité React supplémentaire.

### P3-002 — IA non implémentée

- **Constat** : aucun service, fournisseur ou contrat IA n'existe.
- **Impact** : `REQ-12` et `REQ-13` restent non satisfaites.
- **Action** : choisir le fournisseur et concevoir la frontière backend après sécurisation du cœur métier.

### P3-003 — Déploiement et exploitation absents

- **Constat** : pas de Dockerfile, Compose, health check, logs structurés, monitoring, sauvegarde ou stratégie de rollback.
- **Impact** : le projet n'est pas exploitable en production de façon fiable.
- **Action** : documenter puis automatiser le déploiement après validation du MVP.

## Preuves et limites de l'audit

- Le code source et les documents suivis ont été inspectés.
- Aucun fichier d'environnement n'a été ouvert.
- Les tests Django n'ont pas été exécutés afin de ne pas déclencher un chargement de configuration qui imposerait de consulter des secrets.
- L'état de la base PostgreSQL et des migrations n'a pas été interrogé.
- Les affirmations historiques sur les tests, endpoints et migrations restent à revalider.
