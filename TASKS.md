# TASKS.md — Feuille de Route Opérationnelle

Ce document décrit l'état opérationnel réel. Les éléments marqués « présent » ne signifient pas nécessairement que la fonctionnalité est terminée : ils doivent aussi respecter `DEFINITION_OF_DONE.md`.

## TÂCHES TERMINÉES OU PARTIELLEMENT VALIDÉES

### [TASK-001] Initialisation de l'environnement et des sous-projets

- **Statut** : `PARTIEL — initialisation déclarée, validations d'exécution à effectuer`
- [x] Initialisation Git et configuration du dépôt.
- [x] Initialisation Django avec une configuration PostgreSQL.
- [x] Initialisation React, Vite et Tailwind CSS.

### [TASK-005] Audit documentaire et technique initial

- **Statut** : `TERMINÉ LE 2026-09-25`
- [x] Architecture, backend, frontend, tests et documentation inventoriés.
- [x] Écarts entre vision, documentation et implémentation recensés.
- [x] Priorités de remédiation établies.
- [x] Aucun fichier `.env` ou `.env.*` lu ou analysé.

---

## TÂCHE ACTIVE : [TASK-002] Authentification JWT et modèle utilisateur

- **Objectif** : sécuriser les comptes, JWT et les rôles avant d'exposer les API métier.
- **Statut** : `IN_PROGRESS`

### Réalisé

- [x] Modèle `CustomUser` avec rôle `ADMIN` / `USER`.
- [x] Migration initiale `users.0001_initial` présente dans le dépôt.
- [x] Configuration SimpleJWT avec access token, refresh token et rotation.
- [x] Routes `register`, `me`, `token` et `token/refresh` présentes.
- [x] Cinq tests d'authentification présents dans `users/tests.py`.

### À corriger et à valider

- [ ] Exécuter les tests et consigner date, commande et résultat.
- [ ] Ajouter le logout avec blacklist effective du refresh token.
- [ ] Appliquer réellement les validateurs de mot de passe Django.
- [ ] Empêcher la modification de `is_active` via le profil utilisateur.
- [ ] Ajouter la limitation de débit sur inscription, connexion et refresh.
- [ ] Rendre la configuration fail-closed et interdire un secret Django de secours.
- [ ] Décider du rôle de `role`, `is_staff`, `is_superuser` et d'une éventuelle permission dédiée, puis désigner une autorité administrative unique.
- [ ] Ajouter les tests de permissions, de blacklist, de rotation et de champs sensibles.
- [ ] Vérifier manuellement l'état PostgreSQL, les migrations, l'encodage UTF-8 et les privilèges non superutilisateur du rôle applicatif, sans exposer de secret.

---

## TÂCHE EN PARALLÈLE : [TASK-003] Templates, Documents et modération

- **Objectif** : exposer un domaine métier cohérent, isolé et conforme aux règles de publication.
- **Statut** : `PARTIEL`

### Réalisé

- [x] Modèles `Template` et `Document` avec champs JSONB PostgreSQL.
- [x] Migration initiale `documents.0001_initial` présente dans le dépôt.
- [x] Transitions de statuts codées dans le modèle.
- [x] Actions Django Admin de publication, rejet et archivage.
- [x] Dix tests de modèles présents dans `documents/tests.py`.

### À corriger et à valider

- [ ] Corriger le workflow Django Admin et ne plus masquer les exceptions.
- [ ] Garantir l'initialisation de `created_by` lors de la création d'un modèle.
- [ ] Séparer la publication d'un modèle utilisateur de celle d'un modèle officiel.
- [ ] Créer les serializers, querysets, permissions et endpoints Templates/Documents, dont une file d'attente de modération réservée aux administrateurs.
- [ ] Limiter les brouillons et documents à leur propriétaire.
- [ ] Interdire l'instanciation d'un modèle qui n'est pas `PUBLISHED`.
- [ ] Copier la structure du modèle au lieu de partager le même objet JSON.
- [ ] Valider le schéma des blocs.
- [ ] Définir puis implémenter les index PostgreSQL adaptés aux requêtes réelles.
- [ ] Rendre les transitions atomiques et les protéger contre les écritures concurrentes par un contrôle de version explicite.
- [ ] Ajouter des tests de permissions, d'isolation par propriétaire et de transitions concurrentes.
- [ ] Exécuter les tests et vérifier l'absence de divergence de migrations.

---

## TÂCHE ACTIVE PRIORITAIRE

### [TASK-004] Rétablir un frontend constructible

- **Statut** : `IN_PROGRESS`
- [ ] Corriger `frontend/src/index.css`.
- [ ] Valider le build Vite.
- [ ] Nettoyer le CSS et les assets de template inutilisés.
- [ ] Ajouter une stratégie de tests frontend minimale avant les écrans métier.

## TÂCHES SUIVANTES

### [TASK-006] Layout React et intégration API

- [ ] Ajouter Router, Navbar et pages Login/Dashboard.
- [ ] Centraliser les appels API dans `src/services/`.
- [ ] Définir la stratégie de stockage des tokens, leur renouvellement et la gestion de la déconnexion.
- [ ] Ajouter les états de chargement, erreurs et autorisations.

### [TASK-007] MVP Templates/Documents

- [ ] Implémenter le catalogue des modèles publiés.
- [ ] Permettre la création, la soumission et le suivi d'un modèle personnel.
- [ ] Permettre l'instanciation et l'édition d'un document personnel.
- [ ] Ajouter les exports PDF/Word.

### [TASK-008] Assistance IA

- [ ] Choisir le fournisseur LLM et documenter la décision.
- [ ] Créer le service backend d'assistance par bloc.
- [ ] Garantir que les secrets et JWT ne quittent jamais le backend.

### [TASK-009] Industrialisation

- [ ] Ajouter CI, lint backend, tests frontend et contrôle des migrations.
- [ ] Définir et appliquer une politique reproductible de verrouillage des dépendances Python.
- [ ] Documenter le déploiement, les sauvegardes PostgreSQL et le monitoring.
- [ ] Ajouter une gestion de production fail-closed et des headers de sécurité adaptés.
