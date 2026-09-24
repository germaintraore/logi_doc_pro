. docs/ai/ai-workflow.md (protocole IA)
# AI Workflow — Protocole de Collaboration IA / Développeur

> À faire lire à toute IA avant qu'elle ne modifie `logi_doc_pro`.

## 1. Avant d'agir
1. Lire `PROJECT.md`, `CONSTRAINTS.md`, `STATUS.md`, `TASKS.md`, `ARCHITECTURE.md`.
2. Vérifier `git status` : ne pas écraser un travail non commité sans accord explicite.
3. **NE JAMAIS lire ni afficher** le contenu du fichier `.env` (secrets). Vérifier les valeurs de façon masquée
   (longueurs/encodage), jamais leur valeur.

## 2. Pendant l'écriture
- Implémentation minimaliste : ne modifier que les fichiers de la tâche courante.
- Respecter les règles métier (`docs/business/*`) et les contraintes (`CONSTRAINTS.md`).
- Chaque commande donnée au développeur : ajouter dans `COMMANDS_USE.md` avec justification et explication.
- Ne pas ajouter de commentaires superflus ; expliquer dans la réponse, pas dans le code.

## 3. Après — Validation
- Backend : `python manage.py test` ; Frontend : `npm run lint` puis `npm run build`.
- Mettre à jour `STATUS.md`, `TASKS.md`, `CHANGELOG.md`, et `DECISIONS.md` si choix structurant.
- Vérifier les 6 critères de `DEFINITION_OF_DONE.md`.

## 4. Remontée d'erreurs
- Erreur marquante → entrée dans `docs/ai/known-problems.md` (constat, cause, parade).
- Apprentissage → `docs/ai/lessons-learned.md`.