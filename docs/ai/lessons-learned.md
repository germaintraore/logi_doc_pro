# Lessons Learned — Erreurs et Apprentissages IA

*Ce fichier conserve l'historique des erreurs commises par l'IA ou le développeur pour ne plus jamais les reproduire.*

## [LL-001] Configuration BDD
- **Problème** : Risque d'utilisation par défaut du moteur SQLite par Django.
- **Règle** : Toujours vérifier la variable `DATABASES` dans `settings.py` dès l'initialisation pour pointer vers PostgreSQL.