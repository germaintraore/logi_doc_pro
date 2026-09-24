# STATUS.md — État d'Avancement du Projet

**Dernière mise à jour** : 2026-09-24  
**Phase actuelle** : Phase 1 — Authentification & Modèles de Données

## État des Modules
- [x] Setup Environnement & Git / GitHub : `TERMINÉ`
- [x] Backend Django + PostgreSQL Connection : `TERMINÉ`
- [x] Frontend React + Vite + Tailwind CSS v3 : `TERMINÉ`
- [ ] Module Authentification & Rôles (Admin / User) : `EN COURS` (endpoints `register`, `me`, `token` opérationnels ; tests API à valider)
- [ ] Modèles de Documents & Workflow de Modération : `À FAIRE`
- [ ] Éditeur de Documents par Blocs : `À FAIRE`
- [ ] Intégration Assistant IA : `À FAIRE`

## Contexte Base de Données
- Base `logi_doc_pro` créée (PostgreSQL 18, encodage UTF-8, `OWNER logi_doc_pro_user`).
- Migration `0001_initial` (modèle `CustomUser`) appliquée avec succès.
- ⚠️ Le rôle applicatif doit disposer du privilège `CREATEDB` pour que Django puisse créer `test_logi_doc_pro` lors de `manage.py test` (voir `COMMANDS_USE.md` CMD-024).

## Bloqueurs Actuels
- Privilège `CREATEDB` à accorder à `logi_doc_pro_user` (commande dans `COMMANDS_USE.md`).
- `backend/users/tests.py` à corriger (imports) pour que la suite passe (5 tests).