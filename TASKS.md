# TASKS.md — Feuille de Route & Tâche Active

## TÂCHE EN COURS : [TASK-001]
- **Titre** : Initialisation de l'environnement, Git/GitHub, puis des sous-projets Backend (Django) et Frontend (React).
- **Objectif** : Configurer Git, lier le dépôt distant GitHub, puis initialiser `backend/` et `frontend/`.
- **Statut** : `TERMINÉ` ✅
- [x] **Sous-étape 1** : Initialisation Git local, création de `.gitignore`, premier commit et liaison GitHub. `TERMINÉ`
- [x] **Sous-étape 2** : Initialisation de l'environnement virtuel Python, dépendances et projet Django avec connexion PostgreSQL. `TERMINÉ`
- [x] **Sous-étape 3** : Initialisation du projet React + Vite + Tailwind CSS v3 dans `frontend/`. `TERMINÉ`

---

## TÂCHE EN COURS : [TASK-002]
- **Titre** : Authentification JWT & Modèle Utilisateur Personnalisé.
- **Objectif** : Créer l'app `users` dans Django avec un `CustomUser` gérant les rôles (`ADMIN` / `USER`), configurer `SimpleJWT` et protéger les routes API.
- **Statut** : `IN_PROGRESS`
- [x] `CustomUser` (AbstractUser + champ `role`) — migration `0001_initial` appliquée.
- [x] Config SimpleJWT + routes `token/`, `token/refresh/` (`config/urls.py`).
- [x] Endpoints `register/` et `me/` (`users/urls.py`).
- [ ] `users/tests.py` corrigé et suite de tests au vert (5 tests).
- [ ] Commit de la migration + tests + documentation.

---

## TÂCHES SUIVANTES
- [ ] **[TASK-003]** : Modèles de BDD PostgreSQL (Template, Document) + Workflow de Modération.
- [ ] **[TASK-004]** : Mise en place du layout de base React (Router, Navbar, Pages Login/Dashboard).