# Lessons Learned — Erreurs et Apprentissages IA

*Ce fichier conserve l'historique des erreurs commises par l'IA ou le développeur pour ne plus jamais les reproduire.*

## [LL-001] Configuration BDD
- **Problème** : Risque d'utilisation par défaut du moteur SQLite par Django.
- **Règle** : Toujours vérifier la variable `DATABASES` dans `settings.py` dès l'initialisation pour pointer vers PostgreSQL.

## [LL-002] Rejet de push Git (fetch first / unrelated histories)
- **Problème** : Lors de la création d'un repo GitHub avec initialisation (README/licence), GitHub génère un commit distant indépendant de notre commit local, provoquant l'erreur `[rejected] main -> main (fetch first)`.
- **Règle** : Utiliser `git pull origin main --allow-unrelated-histories --no-rebase` pour fusionner les deux historiques avant de pousser, ou créer le repo GitHub complètement vide.

## [LL-003] Erreur DLL psycopg2 sous Windows (Python 3.8+ / Python 3.14)
- **Problème** : `ImportError: DLL load failed while importing _psycopg` sous Windows provient du fait que depuis Python 3.8, Windows ne recherche plus les DLLs natives (`libpq.dll`) dans le `PATH` système global. De plus, `psycopg` (v3) ne dispose pas encore de wheels binaires précompilés pour Python 3.14 sur PyPI.
- **Règle** : Conserver `psycopg2-binary` et déclarer explicitement le répertoire des binaires PostgreSQL (`C:\Program Files\PostgreSQL\<version>\bin`) via `os.add_dll_directory()` dès l'initialisation de `manage.py` et `config/__init__.py`.