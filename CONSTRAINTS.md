# CONSTRAINTS.md — Contraintes Développeur & Humain

## Contraintes d'Apprentissage & Pédagogie
- **Accompagnement** : Le développeur utilise l'IA comme un accélérateur mais doit COMPRENDRE chaque ligne.
- **Explications requises** : L'IA doit expliciter les concepts complexes (ex: hooks React, serializers Django, transactions Postgres).
- **Format des commandes** : Fournir des commandes Windows CMD ou Bash ou psql ou Django  explicites et complètes et donne les commandes au developpeurs qui va excuter.
Ajouter toutes les commandes utilisé dans le fichier COMMANDS_USE/md et justifier et expliquer ce que fait cette commande dans cet fichier

## Contraintes Techniques Strictes
- **Backend** : Python 3.10+ / Django / DRF.
- **Frontend** : React (Functional Components + Hooks uniquement, pas de Class Components).
- **Base de données** : PostgreSQL uniquement.
- **Communication** : API REST avec authentification basée sur Tokens (JWT).

## Prodictions (Ce qu'il ne faut JAMAIS faire)
- Pas de bases NoSQL (MongoDB, Redis comme DB principale).
- Pas d'ORM alternatif à Django ORM.
- Ne pas masquer la gestion des erreurs dans le code.