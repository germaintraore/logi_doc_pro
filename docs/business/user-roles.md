# Rôles et Permissions — Matrice RBAC

Ce document sépare les rôles métier souhaités des champs Django actuellement utilisés par le code. L'état initial correspond à l'audit du 2026-09-25.

## 1. Sources d'autorité actuelles

Le modèle `CustomUser` porte plusieurs notions distinctes :

- `role` : rôle métier `ADMIN` ou `USER`, valeur par défaut `USER`.
- `is_staff` : indicateur d'accès à l'administration Django.
- `is_superuser` : indicateur de superutilisateur Django.
- `is_active` : désactivation du compte.

Le serializer de profil expose `role` en lecture seule. En revanche, le workflow Template autorise les actions de modération avec `is_staff` **ou** `is_superuser`. Il en résulte deux anomalies :

- un `role=ADMIN` sans `is_staff` n'est pas reconnu administrateur par le workflow ;
- un `role=USER` avec `is_staff=True` peut être reconnu administrateur par le workflow.

La source de vérité définitive doit être décidée dans `DECISIONS.md` avant de poursuivre les APIs.

## 2. Rôles cibles

### Administrateur métier (`ADMIN`)

- Responsabilité : modérer les modèles et garantir la qualité du catalogue.
- Droits cibles : créer des modèles officiels, examiner les soumissions, ajuster, publier, rejeter et archiver.
- Responsabilités techniques : administrer les comptes si ce droit est explicitement requis.
- État actuel : droit présent dans l'intention produit, mais non appliqué de façon fiable par l'API ou le workflow Admin.

### Utilisateur standard (`USER`)

- Responsabilité : créer et gérer ses documents personnels.
- Droits cibles : consulter les modèles publiés, instancier un modèle, éditer, exporter et supprimer ses propres documents ; gérer ses propres modèles non publiés selon le workflow.
- État actuel : le modèle de données existe, mais les endpoints, querysets et contrôles de propriété ne sont pas exposés.

### Visiteur non authentifié (`ANONYMOUS`)

- Droits cibles : consulter la vitrine publique, créer un compte et se connecter.
- État actuel : l'inscription existe côté API ; le frontend de connexion et la vitrine ne sont pas construits.

## 3. Matrice cible et implémentation

| Action | Visiteur | Utilisateur | Administrateur | État actuel |
|---|:---:|:---:|:---:|---|
| Consulter les modèles publiés | Oui | Oui | Oui | Non exposé par une API métier. |
| Créer un compte | Oui | Oui | Oui | Endpoint présent, validation à compléter. |
| Créer un document personnel | Non | Oui | Oui | Non implémenté. |
| Créer un modèle brouillon | Non | Oui | Oui | Modèle présent, API absente. |
| Soumettre son propre modèle | Non | Oui | Oui, s'il est l'auteur | La transition et le contrôle du créateur existent ; les tests de permissions restent à compléter. |
| Voir un brouillon | Non | Le sien | Selon décision RBAC | Non garanti par queryset. |
| Modifier un brouillon | Non | Le sien | Selon décision RBAC | Non exposé. |
| Démarrer une revue | Non | Non | Oui | Méthode modèle présente, action Admin absente. |
| Publier un modèle | Non | Non | Oui | Action Admin présente mais workflow à corriger. |
| Rejeter avec motif | Non | Non | Oui | Action Admin présente mais exceptions masquées. |
| Archiver un modèle publié | Non | Non | Oui | Action Admin présente, validation à tester. |
| Administrer les comptes | Non | Non | Oui | Non exposé par une permission dédiée. |
| Supprimer ses propres documents | Non | Oui | Oui | Non implémenté. |
| Supprimer les modèles publiés | Non | Non | À décider | Une suppression existe via Django Admin pour le personnel disposant des permissions. La conservation des documents est définie par BR-TMP-05 et `SET_NULL` ; seule la politique de suppression d'un modèle publié reste à décider. |

## 4. Règles de sécurité à appliquer

- Les querysets de Template et Document doivent filtrer par propriétaire avant sérialisation.
- Les objets hors périmètre doivent renvoyer une réponse conforme à la politique DRF choisie, sans révéler l'existence de données sensibles.
- Les permissions doivent être définies dans des classes DRF ou des services partagés, plutôt que dupliquées dans les vues.
- Le rôle ne doit jamais être modifiable par le profil ordinaire.
- La désactivation d'un compte et l'attribution d'un rôle administrateur doivent être des opérations réservées à une autorité explicitement définie.
- Les tests doivent vérifier au minimum l'isolation entre deux utilisateurs et l'interdiction d'escalade de privilèges.

## 5. Décision requise

Choisir puis documenter une stratégie unique parmi :

1. utiliser `role` comme autorité métier et synchroniser les flags Django ;
2. utiliser `is_staff` / `is_superuser` comme autorité technique et conserver `role` comme donnée de profil non autoritaire ;
3. créer une permission dédiée et traiter `role` uniquement comme une donnée de profil.

La stratégie retenue doit être appliquée par migration, serializers, permissions, admin et tests.
