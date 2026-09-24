A. ROADMAP.md
# ROADMAP.md — Feuille de Route Produit

> Vue macro des phases. Les étapes internes vivent dans `TASKS.md`.
> Mettre à jour après chaque milestone.

## Vision
Application web pour concevoir, personnaliser et générer des documents professionnels
structurés, avec assistance IA et modération communautaire des modèles.

## Phases

### Phase 0 — Setup & Architecture ✅ (2026-09-23)
- [x] Git/GitHub, cadrage docs, PostgreSQL, Django+DRF, React+Vite+Tailwind.

### Phase 1 — Authentification & Modèles de Données 🔄 (en cours)
- [ ] [TASK-002] Auth JWT + CustomUser (endpoints OK, tests à valider)
- [ ] [TASK-003] Modèles `Template` et `Document` (JSONB) + workflow de modération
- [ ] [TASK-004] Layout React : Router, Navbar, pages Login/Dashboard

### Phase 2 — Modèles & Modération (prévue)
- [ ] CRUD Templates, file d'attente de modération admin, publication globale

### Phase 3 — Éditeur de Documents par Blocs
- [ ] Éditeur JSONB de sections, export PDF/Word

### Phase 4 — Assistance IA
- [ ] Service backend LLM, assistance contextuelle par bloc

### Phase 5 — Durcissement & Production
- [ ] Sécurité, déploiement, monitoring

## Critères de passage de phase (DEFINITION_OF_DONE.md)
- Tests au vert (backend/frontend) ; `STATUS.md`, `TASKS.md`, `CHANGELOG.md` à jour ;
- aucune dépendance lourde sans justification dans `DECISIONS.md`.