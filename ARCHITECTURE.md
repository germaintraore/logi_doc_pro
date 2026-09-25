# ARCHITECTURE.md — Architecture Cible et État Implémenté

Ce document sépare l'architecture souhaitée de ce qui existe réellement dans le dépôt au 2026-09-25.

## 1. Architecture cible

```text
Navigateur
   │
   ▼
React SPA
   │  API REST JSON + JWT
   ▼
Django / Django REST Framework
   ├── Users & Auth
   ├── Templates & workflow de modération
   ├── Documents
   └── Service IA interne
          │  appel LLM contrôlé
          ▼
     Fournisseur LLM

Django ORM ───────────────► PostgreSQL
```

Le frontend ne doit jamais appeler directement un fournisseur LLM ni manipuler un secret de service. Il ne doit pas non plus conserver un refresh token dans un stockage persistant exposé au script avant que la stratégie de session soit décidée.

## 2. Architecture actuellement observée

```text
React placeholder
   │  aucun client API métier implémenté
   ▼
Routes DRF d'authentification uniquement
   │
   ▼
Django ORM ───────────────► PostgreSQL
```

Le service IA, le client API frontend, les endpoints Templates/Documents et l'infrastructure de déploiement ne sont pas implémentés.

## 3. Responsabilités des domaines

| Domaine | Responsabilité cible | État actuel |
|---|---|---|
| Users / Auth | Comptes, rôles, JWT, profil et permissions | Partiel : modèle, serializers et routes principales présents. |
| Templates | Définition des modèles, soumission et modération | Partiel : modèle et actions Admin présents, API absente. |
| Documents | Instances personnelles et édition par blocs | Partiel : modèle JSONB présent, service métier et API absents. |
| AI Engine | Prompts, appels LLM, validation et gestion des erreurs | Absent. |
| Frontend | Authentification, catalogue, dashboard, éditeur et exports | Scaffold statique uniquement. |
| Infrastructure | Déploiement, migrations contrôlées, monitoring et sauvegardes | Absente. |

## 4. Modèle de données

### Template

Le modèle `documents.Template` contient notamment :

- l'identité, la description et la catégorie ;
- une structure JSONB ;
- le créateur ;
- le statut de workflow ;
- le motif de revue et le reviewer ;
- l'indicateur de modèle officiel ;
- les dates de création et de mise à jour.

La machine d'états implémentée est la suivante :

```text
DRAFT ──submit_for_review──► PENDING_REVIEW
REJECTED ──submit_for_review──► PENDING_REVIEW
PENDING_REVIEW ──withdraw_submission──► DRAFT
UNDER_REVIEW ──withdraw_submission──► DRAFT
PENDING_REVIEW ──start_review──► UNDER_REVIEW
PENDING_REVIEW ──approve(official=true|false)──► PUBLISHED
UNDER_REVIEW ──approve(official=true|false)──► PUBLISHED
PENDING_REVIEW ──reject(note non vide)──► REJECTED
UNDER_REVIEW ──reject(note non vide)──► REJECTED
PUBLISHED ──archive──► ARCHIVED
```

Cette machine ne garantit pas encore l'absence de modifications directes hors des méthodes métier, ni la cohérence en cas d'accès concurrent.

### Document

Le modèle `documents.Document` contient :

- un propriétaire obligatoire ;
- un contenu JSONB ;
- une référence `template` optionnelle ;
- des dates de création et de mise à jour.

Le champ nullable `Document.template` utilise `SET_NULL` : la suppression du template ne supprime pas le document, mais `template_id` devient `NULL`. En revanche, aucun service ne copie actuellement une structure de template publié vers `Document.content`, et rien n'interdit la création manuelle d'un document depuis un template non publié.

## 5. Stockage JSONB

- `Template.structure` et `Document.content` utilisent le champ JSON de Django sur PostgreSQL, ce qui correspond au stockage JSONB.
- Aucun index JSONB GIN ou index spécialisé n'est actuellement déclaré.
- Aucun schéma de validation des blocs n'est appliqué au niveau du modèle ou des serializers.
- L'indexation doit être décidée à partir des requêtes réelles : index générique GIN, index d'expressions ciblées ou absence d'index tant que la charge est faible.

La formulation précédente « structures JSONB indexées » était donc inexacte et est retirée de l'architecture actuelle.

## 6. Authentification et autorisation

### Implémenté

- `CustomUser` hérite d'`AbstractUser` et possède un rôle métier.
- SimpleJWT fournit l'authentification par access et refresh tokens.
- La rotation des refresh tokens et l'application `token_blacklist` sont configurées.
- Les endpoints `register`, `me`, `token` et `token/refresh` existent.

### À compléter

- Logout avec blacklist effective.
- Limitation de débit et protection contre la force brute.
- Validation complète des mots de passe.
- Protection de `is_active` contre la modification par l'utilisateur lui-même.
- Source unique d'autorité administrative.
- Tests de permissions multi-utilisateurs.

## 7. Frontend

Le frontend suit React, Vite et Tailwind CSS, mais ne contient actuellement ni Router, ni client API, ni gestion JWT, ni pages métier. L'interface affiche un statut statique. Une erreur syntaxique dans `frontend/src/index.css` bloque la construction et doit être corrigée avant toute expansion fonctionnelle.

## 8. Sécurité et confidentialité

- Le backend est la seule frontière autorisée pour les accès aux services externes.
- Les fichiers `.env` et `.env.*` sont secrets par principe : l'IA ne doit jamais les ouvrir, les lire ou les analyser.
- La configuration Django de production doit échouer si une variable obligatoire manque et ne doit pas fournir de `SECRET_KEY` de secours.
- `DEBUG` doit être désactivé par défaut.
- Les logs applicatifs ne doivent jamais contenir de JWT, de mot de passe, de secret LLM ou de valeur d'environnement.

## 9. Décisions d'architecture encore ouvertes

- Source de vérité pour l'administration : `role`, `is_staff`, `is_superuser` ou permission dédiée.
- Stratégie de stockage et de renouvellement des tokens côté frontend.
- Schéma de version des blocs et stratégie de migration des documents.
- Stratégie d'indexation JSONB.
- Format et moteur d'export PDF/Word.
- Fournisseur LLM, modèle, limites de débit et politique de conservation des données envoyées.
- Stratégie de déploiement, serveur WSGI, stockage des fichiers exportés et supervision.
