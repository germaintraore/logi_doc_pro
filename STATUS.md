# STATUS.md — État d'Avancement du Projet

**Dernière mise à jour** : 2026-09-25
**Phase actuelle** : Phase 1 — Authentification et fondations du domaine Documents
**Maturité** : prototype précoce, non MVP et non prêt pour la production

## Méthode de lecture de l'état

- **Confirmé** : présence vérifiée dans le code ou résultat d'audit explicitement disponible.
- **Partiel** : une partie du besoin existe, mais des invariants ou parcours essentiels manquent.
- **Non vérifié** : l'élément est documenté précédemment, mais son état réel n'a pas été contrôlé pendant cet audit.
- **Absent** : aucun élément correspondant n'a été trouvé dans le dépôt.

## Synthèse

Le projet dispose d'un cadrage clair, d'un backend Django configuré pour PostgreSQL, de routes JWT et des modèles métier `Template` et `Document`. Le cœur d'authentification reste incomplet, les API métier ne sont pas exposées et le frontend demeure un squelette non livrable en l'état.

## État des modules

| Module | État | Constat au 2026-09-25 |
|---|---|---|
| Cadrage, Git et architecture | Confirmé | Documents de projet présents et dépôt Git exploitable. |
| Backend Django + PostgreSQL | Partiel | Configuration Django/DRF et moteur PostgreSQL présents ; état runtime de la base non vérifié. |
| Frontend React + Vite + Tailwind | Partiel | Scaffold React présent ; ESLint passe, mais `src/index.css` comporte une erreur de syntaxe bloquante. |
| Authentification et rôles | Partiel | `register`, `me`, `token` et `token/refresh` présents ; logout, limitation de débit et cohérence RBAC absents ou incomplets. |
| Modèles Templates/Documents | Partiel | Modèles, migrations, administration Django et 15 tests backend présents ; pas d'API métier ni d'instanciation depuis un modèle publié. |
| Workflow de modération | Partiel | Machine d'états implémentée dans le modèle, mais workflow Django Admin incomplet et erreurs masquées. |
| Éditeur de documents par blocs | Absent | Aucun éditeur ni service frontend métier. |
| Intégration IA | Absent | Aucun module, service ou appel LLM implémenté. |
| Déploiement et supervision | Absent | Aucun manifeste de déploiement, health check, monitoring ou pipeline CI. |

## Validation disponible

- **15 tests backend écrits** : 5 tests dans `users` et 10 tests dans `documents`.
- **Tests backend non exécutés pendant cet audit** : leur résultat actuel n'est donc pas confirmé.
- **ESLint frontend réussi** pendant l'analyse statique.
- **Analyse CSS frontend en échec** : structure CSS invalide détectée dans `frontend/src/index.css`.
- **Build frontend non validé** : il ne doit pas être considéré comme réussi tant que l'erreur CSS n'est pas corrigée.
- **Migrations PostgreSQL non contrôlées** : l'application effective de `users.0001_initial` et `documents.0001_initial` doit être validée séparément par le développeur.
- **Aucun fichier `.env` ou `.env.*` n'a été ouvert, lu ou analysé** pendant cet audit.

## Priorités immédiates

1. Corriger la syntaxe de `frontend/src/index.css`, puis valider le build frontend.
2. Durcir la configuration Django : variables obligatoires, `DEBUG=False` par défaut et aucun secret de secours dans le code.
3. Terminer la sécurité d'authentification : logout avec blacklist, validation des mots de passe, limitation de débit et protection de `is_active`.
4. Décider et appliquer une source unique d'autorité pour l'administration (`role`, `is_staff`, `is_superuser` ou permission dédiée).
5. Concevoir les API Templates/Documents avec isolation par propriétaire et instanciation obligatoire depuis un modèle publié.
6. Exécuter et consigner les validations backend, le check Django et la vérification des migrations.

## Blocages ou dépendances

- L'API métier Templates/Documents doit être définie avant de poursuivre le frontend fonctionnel.
- L'état PostgreSQL et les privilèges du rôle applicatif n'ont pas été vérifiés, car cette vérification ne nécessite pas de prendre connaissance du contenu du fichier d'environnement par l'IA.
- Aucun framework de tests frontend ni workflow CI n'est disponible.

Pour la suite détaillée, consulter `TASKS.md`, `ROADMAP.md` et `docs/ai/known-problems.md`.
