# ROADMAP.md — Feuille de Route Produit

> Vue macro des phases. Le détail exécutable se trouve dans `TASKS.md`.
> La roadmap distingue les fonctions terminées des fondations seulement partiellement présentes.

## Vision

Application web pour concevoir, personnaliser et générer des documents professionnels structurés, avec assistance IA et modération communautaire des modèles.

## Phase 0 — Setup et architecture

**État** : `PARTIEL — fondations déclarées, validations d'exécution non effectuées`

- [x] Cadrage du projet et contraintes techniques.
- [x] Initialisation Git, Django/DRF, React/Vite/Tailwind.
- [x] Configuration PostgreSQL déclarée dans le code.

## Phase 1 — Socle fiable et Auth

**État** : `EN COURS`

- [ ] Corriger l'erreur CSS bloquant le build frontend.
- [ ] Durcir la configuration Django et les secrets de production.
- [ ] Terminer inscription, profil, connexion, refresh et logout.
- [ ] Définir une matrice RBAC cohérente et testée.
- [ ] Ajouter throttling, validation des mots de passe et protection des champs sensibles.
- [ ] Exécuter les tests backend et vérifier les migrations.

### Jalon de sortie

- [ ] Les exigences `REQ-01` à `REQ-04` sont satisfaites.
- [ ] Les tests d'authentification passent et leurs preuves sont consignées.
- [ ] Le frontend se construit sans erreur bloquante.
- [ ] Les écarts de sécurité ouverts sont documentés et bloquants pour la production.

## Phase 2 — API Templates et modération

**État** : `FONDATIONS PARTIELLES`

- [x] Modèles `Template` et `Document` présents.
- [x] Migration initiale et tests de modèles présents.
- [x] Machine d'états codée dans le modèle.
- [ ] API REST Templates avec isolation par propriétaire.
- [ ] File d'attente de modération et permissions administratives.
- [ ] Publication correcte des modèles officiels.
- [ ] Validation du schéma JSON et stratégie d'indexation.

### Jalon de sortie

- [ ] Les exigences `REQ-05` à `REQ-08` sont satisfaites.
- [ ] Un utilisateur ne voit que ses brouillons.
- [ ] Un modèle ne peut être publié que selon le workflow prévu.
- [ ] Les tests de permissions et de workflow passent.

## Phase 3 — MVP Documents

**État** : `NON DÉMARRÉ`

- [ ] Instanciation d'un modèle `PUBLISHED`.
- [ ] Copie indépendante du contenu dans `Document.content`.
- [ ] Édition par blocs avec sauvegarde.
- [ ] Isolation stricte des documents par propriétaire.
- [ ] Exports PDF et Word.
- [ ] Interface React : catalogue, création et édition.

### Jalon de sortie

- [ ] Les exigences `REQ-09` à `REQ-11` sont satisfaites.
- [ ] Un parcours complet « catalogue → document → export » fonctionne.
- [ ] Les tests métier et frontend couvrent le parcours principal.

## Phase 4 — Assistance IA

**État** : `NON DÉMARRÉ`

- [ ] Décision sur le fournisseur LLM.
- [ ] Service IA exclusivement côté backend.
- [ ] Assistance contextualisée sur le bloc sélectionné.
- [ ] Validation, limitation de débit et gestion des erreurs.
- [ ] Tests garantissant l'absence de fuite de secrets ou de JWT.

## Phase 5 — Durcissement et production

**État** : `NON DÉMARRÉ`

- [ ] CI avec lint, tests, migrations et build frontend.
- [ ] Déployer de manière reproductible le backend, le frontend et PostgreSQL.
- [ ] Ajouter health checks, logs, métriques et alerting.
- [ ] Définir les sauvegardes, la restauration et la stratégie de rollback.
- [ ] Documenter API, sécurité, base de données et déploiement.
- [ ] Définir et appliquer une politique reproductible de verrouillage des dépendances Python.

## Ordre d'exécution recommandé

1. Corriger le build frontend.
2. Terminer et tester l'authentification.
3. Trancher le RBAC.
4. Exposer l'API Templates.
5. Sécuriser et tester le workflow de modération.
6. Construire le parcours Document jusqu'à l'export.
7. Ajouter l'assistance IA.
8. Industrialiser et préparer la production.

## Critères de passage de phase

Une phase ne peut être déclarée terminée que si `DEFINITION_OF_DONE.md` est satisfait : compréhension, conformité, gestion d'erreurs, tests pertinents, documentation à jour et absence de dette bloquante. Les tests non exécutés doivent être déclarés comme tels et ne peuvent pas servir de preuve de réussite.
