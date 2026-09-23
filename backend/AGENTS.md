# Instructions Spécifiques Backend (Django)

## Directives
- Utiliser la structure classique de Django Apps pour chaque domaine (`users`, `documents`, `ai_assistant`).
- Toute validation métier doit être effectuée dans les **Serializers** ou les **Models**, jamais dans les Views uniquement.
- Utiliser PostgreSQL `JSONField` pour la structure dynamique des templates de document.