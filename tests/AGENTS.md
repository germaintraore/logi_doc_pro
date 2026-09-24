tests/AGENTS.md
# AGENTS.md — Guide des Tests de `logi_doc_pro`

> Instructions pour écrire/modifier les tests sans les casser.

## Règles d'or
1. Les tests vivent dans `backend/<app>/tests.py` (le dossier `tests/` est réservé à la stratégie).
2. Toujours `rest_framework.test.APITestCase` + `django.urls.reverse(...)` — jamais d'URL en dur.
3. Utiliser `get_user_model()` et `User.objects.create_user(...)` — jamais le `User` par défaut de Django.
4. Ne divulguer aucun secret ni valeur réelle du `.env` dans un test.

## Commandes
```powershell
cd backend
python manage.py test users -v 2    # l'app users
python manage.py test               # toutes les apps
Prérequis
Service postgresql-x64-18 démarré.
Rôle applicatif avec CREATEDB (CMD-024) sinon Django ne peut créer test_logi_doc_pro.
Django crée/détruit la base de test automatiquement ; aucune donnée réelle n'est touchée.
Conventions
Un test = un scénario isolé ; nommer test_<comportement>_<résultat_attendu>.
Tester le succès (201/200) ET les échecs (400/401/403).
Vérifier les données (response.data[...]), pas seulement le code HTTP.
Périmètre
5 tests auth (register OK, mdp court, login tokens, /me 401, /me profil).
À venir : CRUD Templates + modération ; instanciation de Documents (JSONB).