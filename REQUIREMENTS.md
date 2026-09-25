# REQUIREMENTS.md — Exigences Fonctionnelles et Non Fonctionnelles

> Source de vérité des exigences. Chaque exigence possède un identifiant stable de la forme `REQ-N` ou `REQ-NF-N`.
> L'état ci-dessous décrit l'implémentation constatée par audit statique au 2026-09-25 ; il ne remplace pas une preuve d'exécution.

## Légende

| État | Signification |
|---|---|
| `TERMINÉ` | Besoin satisfait et preuve de validation disponible. |
| `PARTIEL` | Une partie du besoin est codée, mais des éléments essentiels manquent. |
| `À FAIRE` | Besoin non implémenté. |
| `NON VÉRIFIÉ` | L'état réel ne peut pas être confirmé sans une validation manuelle. |
| `NON CONFORME` | L'état observé ne respecte pas l'exigence. |

## 1. Exigences fonctionnelles

### 1.1 Authentification et comptes

| ID | Exigence | État | Implémentation constatée / écart |
|---|---|---|---|
| REQ-01 | Permettre la création d'un compte avec username, email obligatoire et unique, et mot de passe d'au moins 12 caractères. | `PARTIEL` | L'endpoint existe et la longueur minimale est codée ; l'email reste facultatif et non unique, et les validateurs Django complets ne sont pas appliqués. |
| REQ-02 | Permettre la connexion et renvoyer un access token et un refresh token JWT. | `PARTIEL` | Les routes SimpleJWT sont présentes ; leur exécution actuelle n'a pas été revérifiée pendant l'audit. |
| REQ-03 | Permettre le refresh et la déconnexion avec blacklist du refresh token. | `PARTIEL` | Le refresh et sa rotation sont configurés ; aucun endpoint de logout avec blacklist n'est exposé. |
| REQ-04 | Donner à chaque compte un rôle `ADMIN` ou `USER`, non modifiable par lui-même. | `PARTIEL` | Le champ `role` est en lecture seule dans le serializer, mais les autorisations admin utilisent `is_staff` ou `is_superuser` ; `is_active` reste modifiable par le profil. |

### 1.2 Templates

| ID | Exigence | État | Implémentation constatée / écart |
|---|---|---|---|
| REQ-05 | Permettre à un administrateur de créer, modifier, archiver et publier des modèles officiels. | `PARTIEL` | Des actions Admin existent, mais le workflow officiel est incomplet et aucune API n'est exposée. |
| REQ-06 | Permettre à un utilisateur de créer un brouillon, de le soumettre et d'annuler une soumission non rejetée. | `PARTIEL` | Les transitions de modèle existent ; les endpoints et la protection contre la modification directe des champs manquent. |
| REQ-07 | Permettre à un administrateur d'examiner, ajuster, publier ou rejeter un modèle avec motif. | `PARTIEL` | La machine d'états et certaines actions Admin existent ; il n'y a ni file d'attente API, ni historique de revue, ni action de début de revue dans l'interface Admin. |
| REQ-08 | Montrer un brouillon uniquement à son créateur et conserver la paternité. | `PARTIEL` | Le champ `created_by` existe ; aucun queryset métier n'assure encore la visibilité privée. |

### 1.3 Documents

| ID | Exigence | État | Implémentation constatée / écart |
|---|---|---|---|
| REQ-09 | Créer un document uniquement à partir d'un modèle publié. | `À FAIRE` | Aucun service ni endpoint d'instanciation ; l'invariant n'est pas garanti. |
| REQ-10 | Stocker le document en JSONB de façon indépendante du modèle source. | `PARTIEL` | `Document.content` est JSONB et le document survit à la suppression du template grâce à `SET_NULL`, mais `template_id` devient `NULL` ; aucun mécanisme de copie contrôlée n'est implémenté. |
| REQ-11 | Permettre à un utilisateur d'éditer, exporter en PDF/Word et supprimer ses propres documents. | `À FAIRE` | Aucune API CRUD Document, aucun export ni contrôle de propriété orienté utilisateur n'est exposé ; `DocumentAdmin` permet toutefois certaines opérations sur les objets existants, sous permissions Django. |

### 1.4 Assistance IA

| ID | Exigence | État | Implémentation constatée / écart |
|---|---|---|---|
| REQ-12 | Fournir une aide IA au niveau du bloc sélectionné. | `À FAIRE` | Aucun module ou service IA. |
| REQ-13 | Effectuer les appels LLM uniquement côté backend, sans exposer JWT ni secrets. | `À FAIRE` | Aucun appel LLM n'est implémenté ; le fournisseur et son architecture restent à décider. |

## 2. Exigences non fonctionnelles

| ID | Exigence | État | Implémentation constatée / écart |
|---|---|---|---|
| REQ-NF1 | Utiliser PostgreSQL exclusivement. | `TERMINÉ` | Django référence PostgreSQL et aucun fallback SQLite n'a été trouvé. |
| REQ-NF2 | Exposer une API REST DRF en JSON avec authentification JWT. | `PARTIEL` | DRF et JWT sont configurés pour l'authentification ; les API métier et le versionnement sont absents. |
| REQ-NF3 | Garder les secrets hors du dépôt, ne fournir aucun secret de secours en code et utiliser un rôle PostgreSQL non superutilisateur. | `NON CONFORME` | La configuration Django contient une valeur de secours pour `SECRET_KEY` ; l'environnement et les privilèges du rôle PostgreSQL restent à vérifier manuellement, sans transmettre leurs valeurs. |
| REQ-NF4 | Utiliser UTF-8 pour préserver les accents. | `NON VÉRIFIÉ` | La documentation antérieure indique une base UTF-8, mais l'encodage réel n'a pas été contrôlé pendant cet audit. |
| REQ-NF5 | Garder les erreurs lisibles et ne pas les masquer. | `NON CONFORME` | Les actions Django Admin ignorent des `ValidationError` et peuvent afficher un succès partiel trompeur. |
| REQ-NF6 | Stocker le contenu documentaire en JSONB et définir une stratégie d'indexation fondée sur les requêtes et la charge mesurées. | `PARTIEL` | Les champs JSONB existent, mais aucune stratégie d'indexation n'est encore justifiée par des mesures ni implémentée. |

## 3. Règles d'acceptation transverses

- Toute route métier doit limiter les querysets au propriétaire, sauf permission administrative explicite.
- Toute transition d'état doit être centralisée, transactionnelle et protégée contre les transitions concurrentes invalides.
- Toute erreur doit être journalisée et retournée sous une forme exploitable, sans exposer de secret.
- Les tests doivent couvrir les cas nominaux, le refus d'accès et les erreurs métier.
- Les résultats non exécutés doivent être datés et accompagnés de la commande réellement utilisée dans un registre de validation versionné avec le projet.

## 4. Hypothèses produit

- Chaque utilisateur standard ne voit et ne modifie que ses propres modèles non publiés et ses documents personnels, sous réserve des permissions administratives explicites définies par la matrice RBAC.
- La modération concerne les modèles, pas le contenu des documents personnels.
- Les modèles publiés constituent la seule source autorisée pour créer un document.
- Le fournisseur LLM, le format d'export et l'infrastructure de production restent à décider.
