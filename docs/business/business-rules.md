# Règles Métier — Templates et Documents

Ce document distingue les règles de domaine confirmées des invariants qui doivent encore être protégés dans le code. L'état décrit correspond à l'audit du 2026-09-25.

## 1. Cycle de vie d'un Template

### Machine d'états implémentée

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

### Transitions autorisées par le modèle actuel

| État courant | Action | État suivant | Autorité actuellement codée |
|---|---|---|---|
| `DRAFT` | Soumettre | `PENDING_REVIEW` | Créateur du template. |
| `REJECTED` | Corriger et soumettre | `PENDING_REVIEW` | Créateur du template. |
| `PENDING_REVIEW` | Annuler | `DRAFT` | Créateur du template. |
| `UNDER_REVIEW` | Annuler | `DRAFT` | Créateur du template. |
| `PENDING_REVIEW` | Démarrer la revue | `UNDER_REVIEW` | `is_staff` ou `is_superuser`. |
| `PENDING_REVIEW` | Publier | `PUBLISHED` | `is_staff` ou `is_superuser`. |
| `UNDER_REVIEW` | Publier | `PUBLISHED` | `is_staff` ou `is_superuser`. |
| `PENDING_REVIEW` | Rejeter avec motif | `REJECTED` | `is_staff` ou `is_superuser`. |
| `UNDER_REVIEW` | Rejeter avec motif | `REJECTED` | `is_staff` ou `is_superuser`. |
| `PUBLISHED` | Archiver | `ARCHIVED` | `is_staff` ou `is_superuser`. |

La documentation utilise les six états du modèle : `DRAFT`, `PENDING_REVIEW`, `UNDER_REVIEW`, `REJECTED`, `PUBLISHED` et `ARCHIVED`. `MODIFIED` n'est pas une valeur de `Template.Status`.

## 2. Règles de gestion des Templates

| ID | Règle de domaine | État technique |
|---|---|---|
| BR-TMP-01 | Un modèle `DRAFT`, `PENDING_REVIEW`, `UNDER_REVIEW`, `REJECTED` ou `ARCHIVED` est visible par son seul créateur, sauf permission administrative explicite. | `À IMPLEMENTER` : aucun queryset métier n'existe encore. |
| BR-TMP-02 | Un modèle soumis ne peut plus être modifié directement par son auteur sans annuler la soumission. | `PARTIEL` : la transition de retrait existe, mais aucune garde sur les champs ne l'impose. |
| BR-TMP-03 | Un administrateur peut ajuster le contenu d'un modèle soumis avant publication. | `PARTIEL` : l'accès Django Admin existe, mais la source d'autorité RBAC et le workflow sont à clarifier. |
| BR-TMP-04 | La paternité du modèle est conservée malgré les retouches administratives. | `PARTIEL` : `created_by` existe, mais le workflow de création Admin ne l'initialise pas de façon fiable. |
| BR-TMP-05 | Un document existant reste indépendant d'un modèle publié puis archivé ou supprimé. | `PARTIEL` : `SET_NULL` protège le document et le contenu est JSONB, mais le mécanisme de copie n'est pas encore codé. |
| BR-TMP-06 | Seul un modèle `PUBLISHED` peut servir de source à un nouveau document. | `À IMPLEMENTER` : aucun service ou serializer ne garantit cet invariant. |
| BR-TMP-07 | Toute transition doit être atomique et refusée si l'état a changé entre-temps. | `À IMPLEMENTER` : aucun verrouillage optimiste ou contrôle de version n'est présent. |

## 3. Règles de gestion des Documents

1. Un Document possède un propriétaire obligatoire.
2. Un Document ne doit être accessible et modifiable que par son propriétaire, sauf permission administrative explicite.
3. `Document.content` doit contenir une copie indépendante de la structure du modèle source.
4. Le Document ne doit pas partager une structure Python mutável avec le Template.
5. La suppression du Template source ne doit pas supprimer le Document.
6. Les opérations d'export doivent produire un fichier contrôlé et conforme au format choisi.

## 4. Structure des blocs

Le schéma de référence envisagé est composé de blocs de types suivants :

- Titre ou en-tête.
- Paragraphe ou Markdown enrichi.
- Liste à puces ou numérotée.
- Tableau structuré.
- Métadonnées ou champ contextualisé.

Ces types sont une intention de conception, pas un contrat sérialisé déjà appliqué par le backend.

## 5. Assistance IA

- L'IA doit intervenir sur un bloc explicitement sélectionné.
- Les appels LLM doivent être réalisés par le backend.
- Le frontend ne doit jamais recevoir de secret fournisseur.
- Les erreurs du fournisseur doivent être converties en erreurs fonctionnelles lisibles, sans exposer de prompt interne, de secret ou de stack trace de production.

## 6. Points à valider par tests

- Un utilisateur ne peut pas lire ou modifier un modèle non publié appartenant à un autre utilisateur.
- Un utilisateur ne peut pas transitionner un Template qui n'est pas le sien.
- Un modèle dans un statut autre que `PUBLISHED` ne peut pas initialiser un Document.
- Une transition concurrente invalide est rejetée.
- Une erreur de publication ne produit pas de faux message de succès.
- La suppression d'un Template ne modifie pas le contenu d'un Document existant.
