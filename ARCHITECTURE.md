# ARCHITECTURE.md — Conception Système

## Flux de Données
[Client React] <---> [API REST Django DRF] <---> [PostgreSQL]
                               │
                               └───> [Service IA / LLM]

## Structure des Domaines
1. **Users / Auth** : Gestion des comptes, rôles et authentification JWT.
2. **Templates** : Modèles de documents préconfigurés (CV, Cahier des charges, etc.).
3. **Documents** : Instances de documents créées par les utilisateurs (stockés sous forme de blocs JSON).
4. **AI Engine** : Service interne Django gérant le prompt engineering et les appels aux API LLM.

## Format des Documents
Les documents sont stockés en base PostgreSQL sous forme de structures JSONB indexées pour garantir une flexibilité totale des sections tout en maintenant des performances élevées.