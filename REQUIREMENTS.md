 REQUIREMENTS.md
# REQUIREMENTS.md — Exigences Fonctionnelles & Non-Fonctionnelles

> Source de vérité des exigences. Chaque exigence porte un identifiant traçable (REQ-xx).

## 1. Exigences Fonctionnelles

### 1.1 Authentification & Comptes
- [REQ-01] Un visiteur peut créer un compte (username, email, mot de passe ≥ 12 caractères).
- [REQ-02] Un utilisateur se connecte (username + password) et reçoit un access + refresh token JWT.
- [REQ-03] Un utilisateur rafraîchit son access token et se déconnecte (blacklist du refresh).
- [REQ-04] Chaque compte possède un rôle `ADMIN` ou `USER` (défaut `USER`), jamais modifiable par soi-même via l'API (read_only).

### 1.2 Modèles (Templates)
- [REQ-05] L'admin crée, modifie, archive et publie des modèles officiels.
- [REQ-06] Un utilisateur crée un modèle en brouillon (`DRAFT`), le soumet (`PENDING_REVIEW`), peut annuler la soumission tant que non rejeté (BR-TMP-02).
- [REQ-07] L'admin examine la file d'attente, ajuste, valide (`PUBLISHED`) ou rejette (`REJECTED`) avec motif.
- [REQ-08] Un brouillon n'est visible que par son créateur (BR-TMP-01) ; la paternité est conservée (BR-TMP-04).

### 1.3 Documents
- [REQ-09] Un utilisateur instancie un modèle publié pour créer un document personnel.
- [REQ-10] Un document est stocké en JSONB, indépendant du modèle source (BR-TMP-05).
- [REQ-11] Un utilisateur édite, exporte (PDF/Word) et supprime ses propres documents.

### 1.4 Assistance IA
- [REQ-12] L'IA agit au niveau du bloc sélectionné : reformulation, correction de style, génération guidée (BR-DOC-03).
- [REQ-13] L'IA n'accède jamais aux tokens JWT ni aux secrets ; appels gérés côté backend uniquement.

## 2. Exigences Non-Fonctionnelles
- [REQ-NF1] Base de données : PostgreSQL uniquement (interdiction SQLite/MongoDB, cf. CONSTRAINTS.md).
- [REQ-NF2] API : REST + DRF, JSON, authentification JWT.
- [REQ-NF3] Sécurité : secrets uniquement via `.env` (jamais versionné) ; rôle BDD sans superuser.
- [REQ-NF4] Encodage : base créée en UTF-8 pour un support correct des accents.
- [REQ-NF5] Débogage : les erreurs exceptionnelles doivent rester lisibles (parade KP-001).
- [REQ-NF6] Perf : contenu documentaire en `jsonb` indexé.

## 3. Hypothèses
- Multi-tenant strict : un utilisateur ne voit que ses documents et brouillons.
- La modération concerne les modèles uniquement (pas les documents personnels).