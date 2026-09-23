# Rôles et Permissions — Matrice RBAC

Ce document définit les rôles au sein de `logi_doc_pro` et leurs permissions respectives sur les Modèles (Templates) et les Documents.

---

## 1. Définition des Rôles

### A. Administrateur (`ADMIN` / `STAFF`)
- **Responsabilité** : Garantir la qualité, la cohérence et la sécurité des modèles disponibles sur la plateforme.
- **Droits spécifiques** :
  - Créer, modifier, archiver et supprimer des modèles officiels (`is_official = True`).
  - Consulter la file d'attente des modèles soumis par les utilisateurs (`status = PENDING_REVIEW`).
  - Modifier/ajuster le contenu ou la structure d'un modèle soumis par un utilisateur avant de le publier.
  - Valider (`status = PUBLISHED`) ou rejeter (`status = REJECTED`) un modèle avec message d'explication.
  - Administrer les comptes utilisateurs.

### B. Utilisateur Standard (`USER`)
- **Responsabilité** : Créer et gérer ses propres documents professionnels.
- **Droits spécifiques** :
  - Explorer et rechercher dans le catalogue des modèles publiés (`status = PUBLISHED`).
  - Instancier un modèle pour générer un document personnel.
  - Éditer, sauvegarder, exporter (PDF/Word) et supprimer ses propres documents.
  - Concevoir un nouveau modèle de document personnalisé en mode brouillon (`status = DRAFT`).
  - Soumettre son modèle personnel à la revue administrateur (`status = PENDING_REVIEW`).
  - Modifier ou supprimer ses modèles tant qu'ils n'ont pas encore été validés/publiés.

### C. Visiteur / Non Authentifié (`ANONYMOUS`)
- **Droits spécifiques** :
  - Consulter la page d'accueil et la vitrine des modèles publics.
  - Créer un compte ou se connecter.

---

## 2. Matrice Récapitulative des Droits

| Entité / Action | Visiteur | Utilisateur | Administrateur |
|---|:---:|:---:|:---:|
| **Voir les modèles publiés** | Lecture seule | Lecture | Lecture |
| **Créer un document personnel** | ❌ | ✅ | ✅ |
| **Créer un modèle (brouillon)** | ❌ | ✅ | ✅ |
| **Soumettre un modèle à la revue**| ❌ | ✅ | N/A (direct) |
| **Revoir / Ajuster un modèle soumis** | ❌ | ❌ | ✅ |
| **Publier un modèle officiel** | ❌ | ❌ | ✅ |
| **Rejeter un modèle soumis** | ❌ | ❌ | ✅ |
